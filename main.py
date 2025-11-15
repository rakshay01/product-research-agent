from src.graph import app

def main():
    print("\n=== Product Research Agent ===")
    query = input("Enter your query: ")

    print("\nRunning agent...\n")
    result = app.invoke({"query": query})

    print("\n=== FINAL RESULT ===")
    print(result["answer"])
    print("====================\n")

if __name__ == "__main__":
    main()
