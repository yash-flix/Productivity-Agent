from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class ExcelService:

    def __init__(self):
        self.output_dir = Path("outputs/reports")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def load_file(self, file_path: str):

        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)

        elif file_path.endswith(".xlsx"):
            return pd.read_excel(file_path)

        else:
            raise ValueError("Unsupported file format.")

    def clean_data(self, df: pd.DataFrame):

        df = df.drop_duplicates()

        numeric_cols = df.select_dtypes(include="number").columns
        text_cols = df.select_dtypes(exclude="number").columns

        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].median())

        for col in text_cols:
            df[col] = df[col].fillna("N/A")

        return df

    def summary(self, df):

        return df.describe(include="all")

    def missing_values(self, df):

        return df.isnull().sum()

    def correlation(self, df):

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return None

        return numeric.corr()

    def top_values(self, df, column):

        return df[column].value_counts().head(10)

    def pivot_table(self, df, index, values):

        return pd.pivot_table(
            df,
            index=index,
            values=values,
            aggfunc="sum"
        )

    def create_bar_chart(
        self,
        df,
        group_column,
        value_column
    ):

        grouped = (

            df.groupby(group_column)[value_column]

            .sum()

        )

        plt.figure(figsize=(10, 6))

        grouped.plot(kind="bar")

        plt.tight_layout()

        chart_path = (
            self.output_dir
            / f"{group_column}_{value_column}.png"
        )

        plt.savefig(chart_path)

        plt.close()

        return str(chart_path)

    def export_report(
        self,
        cleaned_df,
        summary_df,
        pivot_df
    ):

        output_path = (
            self.output_dir
            / "analysis.xlsx"
        )

        with pd.ExcelWriter(
            output_path,
            engine="openpyxl"
        ) as writer:

            cleaned_df.to_excel(
                writer,
                sheet_name="Cleaned Data",
                index=False
            )

            summary_df.to_excel(
                writer,
                sheet_name="Summary"
            )

            if pivot_df is not None:
                pivot_df.to_excel(
                    writer,
                    sheet_name="Pivot"
                )

        return str(output_path)