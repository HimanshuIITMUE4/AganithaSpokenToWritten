
# Spoken To Written

This Python module converts a paragraph of spoken english to written english.

 For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.


## Installation:


  Please ensure that you have **updated pip3** to the latest version before installing spoken2written.
  
  You can install the module using Python Package Index using the below command.
   ```
   >>python3 setup.py install
   ```


## Usage:


**Correct one:**
   ```
    >>python3
	>>from SpokenToWritten import sp2wr
	>>spoken2written.convert_sp_to_wr()
	>>
	[IN]:Enter Your paragraph of spoken english:
	" You owe me three hundred dollars. Give me the money and I will give you three percent of that."

[Input]: The Spoken English Paragraph: 

 " " You owe me three hundred dollars. Give me the money and I will give you three percent of that.""


--------------------***************--------------------


[Output]: Converted Written English Paragraph: 

 " " You owe me3 $100 Give me the money and I will give you3 % of that.""
```
	
	
**Wrong One:**

    >>python3
	>> from SpokenToWritten import sp2wr
	>> spoken2written.convert_sp_to_wr()

	[IN]:Enter Your paragraph of spoken english:
	My phone number is double 5, triple 4, 5 times 8 and 5 times 3.

[Input]: The Spoken English Paragraph: 

 " My phone number is double 5, triple 4, 5 times 8 and 5 times 3."


--------------------***************--------------------


[Output]: Converted Written English Paragraph: 

 " My phone number is 55, 444, 5 times 8 and 5 times 3."
 

## Note: 

   **For the Above input paragraph the incorrect output was as a result of improper use of words like 'times' to describe the phone number and spaces after '.' and ','. Currently this code can convert a given set of english spoken paragraph due to limitations on defined rules. But as more rules are added, code can be written to adjust the sentences accordingly.**



## Bugs/Errors

   If you find any bugs/errors in the usage of above code, please raise an issue through  
   [Github](https://github.com/HimanshuIITMUE4/AganithaSpokenToWritten)


## Here are some possible future functionalities that  can be covered in the future versions of the module:

1.   If the paragraph contains a money figure e.g. two million three thousand nine hundred and eighty-four then we may convert it to numbers as 2003984.

2. Handling of both American number system and Indian number system e.g. million, lakhs.

3.  Handling of Dates e.g. Today's Date is twenty-eight October two thousand twenty as Today's Date is 28-10-2020/2020-10-28.

4. Handling of Punctuation.

5. Handling of proper spaces after one sentance.

6. Handling of various mathematical signs can also be incorporated

7. Also we can handle any specific email address spoken with all the '@', '.', or '-'.


**Please, Feel free to connect if you have some ideas.**


## License


MIT License

Copyright (c) 2019 Vishal Dhiman  [Github](https://github.com/cyberdhiman/Spoken-To-Written-English)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

