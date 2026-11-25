import pandas as pd


def main():
    print("running with docker bind mount!")
    df = pd.read_csv('data.csv')
    print("\n === Dataset === ")
    print(df)

    print("\n === Summary Statistics ===")
    print(df.describe())

    print("\n Department Wise Analysis")

    dept_summary = (df.groupby(['department']).agg(
        avg_salary = ("salary", "mean"), 
        avg_experience = ("experience", "mean"), 
        employee_count = ("employee", "count"),
    ).round(2)
    )
    print(dept_summary)

    print("\n Application Executed Successfully !")

    print("edited the file..")

    print("little change to app.py")

if __name__ == "__main__":
    main()