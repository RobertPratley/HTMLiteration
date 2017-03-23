In-browser Font iteration test

What is this?

This script is a quick/work in progress method to quickly generate multiple versions of a html template so as to be quickly able to test iterations on screen in the early typeface design process.

It is dependent on the following file structure:

|-- Testing Folder
        |-- buildHTMLIteration.py
        |-- template.html (HTML to be _iterated_)
        |-- style.css (self defined)
        |-- fonts
              |-- other (fonts not for testing)
              |-- testing (fonts to iterate through)

The script writes a new output html file (default: testsite.html, changeable in the python code) by looping through the fonts in fonts/testing and importing the template.html file the necessary number of times. A new fonts.css file is also created with the necessary @font-face rules. Subsequently, the import of fonts.css should be called in your style.css file. Each iteration in the output html is wrapped in a <div> that specifies the test font to be used for that iteration. 

template.html shoudl not include the opening or closing <body> tag, or the <head> information. This is defined in the python and written during generation. Changes to this information can be made easily in buildHTMLIteration.py.

###To run:

Ensure you have the necessary files in the structure defined above, then cd to the directory containing these files and run: python buildHTMLIteration.py 

Alternatively, you an open the python file in a code editor and build from there. 


