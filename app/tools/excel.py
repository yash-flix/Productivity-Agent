from langchain_core.tools import tool

from app.services.excel_service import ExcelService

service = ExcelService()


@tool
def analyze_excel(
    file_path: str,
    analysis_type: str = "summary"
) -> str:
    """
    Analyze an Excel or CSV file.

    analysis_type:
    summary
    pivot
    chart
    correlation
    missing_values
    top_values
    """

    try:

        df = service.load_file(file_path)

        cleaned = service.clean_data(df)

        print("\n========== DTYPES ==========")
        print(cleaned.dtypes)
        print("============================\n")

        numeric_columns = list(
            cleaned.select_dtypes(include="number").columns
        )

        categorical_columns = list(
            cleaned.select_dtypes(exclude="number").columns
        )

        summary = service.summary(cleaned)

        result = ""

        chart = None

        pivot = None

        if analysis_type == "summary":

            result = summary.to_string()

        elif analysis_type == "missing_values":

            result = service.missing_values(cleaned).to_string()

        elif analysis_type == "correlation":

            corr = service.correlation(cleaned)

            if corr is None:
                result = "No numeric columns found."

            else:
                result = corr.to_string()

        elif analysis_type == "top_values":

            if not categorical_columns:
                result = "No categorical columns found."

            else:

                result = service.top_values(
                    cleaned,
                    categorical_columns[0]
                ).to_string()

        elif analysis_type == "pivot":

            if not numeric_columns:

                return "No numeric columns found."

            if not categorical_columns:

                return "No categorical columns found."

            pivot = service.pivot_table(

                cleaned,

                index=categorical_columns[0],

                values=numeric_columns[0]

            )

            result = pivot.to_string()

        elif analysis_type == "chart":

            if not numeric_columns:

                return "No numeric columns found."

            if not categorical_columns:

                return "No categorical columns found."

            chart = service.create_bar_chart(

                cleaned,

                categorical_columns[0],

                numeric_columns[0]

            )

            result = f"Chart saved to {chart}"

        else:

            result = summary.to_string()

        if (
            numeric_columns
            and
            categorical_columns
        ):

            pivot = service.pivot_table(

                cleaned,

                index=categorical_columns[0],

                values=numeric_columns[0]

            )

        report = service.export_report(

            cleaned,

            summary,

            pivot

        )

        return f"""
Excel Analysis Complete

Rows:
{len(cleaned)}

Columns:
{list(cleaned.columns)}

Analysis:
{analysis_type}

----------------------------------

{result}

----------------------------------

Chart:
{chart}

Excel Report:
{report}
"""

    except Exception as e:

        import traceback

        traceback.print_exc()

        return str(e)