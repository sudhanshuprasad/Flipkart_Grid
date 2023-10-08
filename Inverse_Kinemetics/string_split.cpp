#include <iostream>
#include <string>

std::string* splitString(const std::string& inputString, char delimiter, int& size) {
    int count = 1;
    for (char c : inputString) {
        if (c == delimiter) {
            count++;
        }
    }

    std::string* result = new std::string[count];
    int index = 0;
    std::string item;

    for (char c : inputString) {
        if (c == delimiter) {
            result[index++] = item;
            item.clear();
        } else {
            item += c;
        }
    }

    // Add the last item if it exists
    if (!item.empty()) {
        result[index++] = item;
    }

    size = count;
    return result;
}

int main() {
    std::string input = "Hello,World,OpenAI,GPT-3.5 Turbo";
    int size = 0;
    std::string* splitResult = splitString(input, ',', size);

    for (int i = 0; i < size; i++) {
        std::cout << splitResult[i] << std::endl;
    }

    delete[] splitResult;

    return 0;
}