import sys
import pandas as pd

def compare_houses(file1, file2):
    # Read both CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Check if files have same number of rows
    if len(df1) != len(df2):
        print(f"Error: Files have different lengths ({len(df1)} vs {len(df2)})")
        return
    
    # Compare houses
    correct = 0
    total = len(df1)
    
    for i in range(total):
        if df1['Hogwarts House'][i] == df2['Hogwarts House'][i]:
            correct += 1
    
    # Calculate accuracy
    accuracy = correct / total
    
    # Print results
    print(f"Total predictions: {total}")
    print(f"Correct predictions: {correct}")
    print(f"Wrong predictions: {total - correct}")
    print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare.py file1.csv file2.csv")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    
    try:
        compare_houses(file1, file2)
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except KeyError:
        print("Error: CSV files must have 'Hogwarts House' column")
    except Exception as e:
        print(f"Error: {e}")