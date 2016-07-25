# markov_chain


This is an implementation of a [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) that generates random text based on content provided by the user. 

## How to use the Markov Chain text generator
1. After importing this cc_markov into your main project script, create an instance of MarkovChain and assign it to a variable. For example `mc = MarkovChain()`
2. Use one of the methods to read a local text file or a string. You can call this method multiple times to add additional data.
3. Call the `generate_text()` function on the instance of MarkovChain you created to generate text from the Markov Chain. You can call this method multiple times to generate additional data. This function will output a list of words. If your project requires a different format, you should convert the output accordingly.


## License

This code is currently under the terms of the GPL v2 License which you can read about in the LICENSE file. This means it is free to use, copy, distribute, and modify, but you must disclose the original code and copyright under the same terms.
