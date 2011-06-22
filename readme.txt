wxspreadsheet.py: basic wxPython Spreadsheet control

wxspreadsheet is a simple single file extension to wxPython's CSheet (grid) control that offers basic spreadsheet functionality.  The CSheet control provides most of the basics but wxspreadsheet offers a few extra niceties:

- simple context (right-click) menu for inserting / deleting rows and columns
- response to arrow keys and Enter more closely match typical spreadsheet behavior by accepting edits in a cell and moving appropriately
- includes methods for reading and writing to CSV files

In this version of wxspreadsheet, Python's csv module is used to read/write CSV files.  You may want to write your own I/O methods or better yet use Numpy's loadtxt/savetxt methods as more flexible alternatives.

Also included in this repo is a simple demonstration program, wxspreadsheet_demo.py.  The demo is a pared down spreadsheet-type application that can open and save CSV files; nothing fancy but hopefully illustrative of how wxspreadsheet can be used in your applications.

Chris Coughlin
June 21 2011