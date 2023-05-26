from ranked_results import compute_similarity, load_cleaned_data


def main():
    # Prompt the user for input text and the number of similar items
    input_text = input("Type your desired clothing item: ")
    top_n = int(input("How many results do you wish to see?: "))

    # Load the cleaned data
    database = load_cleaned_data('cleaned_data.json')

    # Compute similarity and get ranked results
    ranked_results = compute_similarity(input_text, database, top_n)

    # Print the ranked results
    print("Ranked Results:")
    for i, result in enumerate(ranked_results, 1):
        print(f"{i}. {result}")

if __name__ == '__main__':
    main()
