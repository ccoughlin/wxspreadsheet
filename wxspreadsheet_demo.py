#!/usr/bin/env python
"""wxspreadsheet_demo.py: Demonstration of the wxspreadsheet control"""


import wx
import wxspreadsheet


__author__ = "Chris Coughlin"
__copyright__ = "Copyright 2011, Chris Coughlin"
__credits__ = ['Chris Coughlin']
__license__ = "BSD"
__version__ = "06.15.11"
__maintainer__ = "Chris Coughlin"
__email__ = "chriscoughlin@gmail.com"
__status__ = "Prototype"


class wxSpreadSheetDemo(wx.Frame):
    '''Simple user interface to demo the wxSpreadsheet control'''
    widget_margin = 3.0 # Default border around widgets
    label_pct = 0.25 # Default resizing factor for labels - 25%
    ctrl_pct = 1.0 # Default resizing factor for controls - 100%
    sizer_flags = wx.ALL | wx.EXPAND # Default resizing flags for controls

    def __init__(self, parent=None):
        wx.Frame.__init__(self, id=wx.ID_ANY, name='', parent = parent,
            title='wxSpreadsheet Demonstration')
        self.init_menu()
        self.init_ui()
        self.Bind(wx.EVT_CLOSE, self.on_quit)

    def init_menu(self):
        '''Creates the program menu'''
        self.menubar = wx.MenuBar()
        self.file_mnu = wx.Menu() # File Menu
        self.open_file_mnui = wx.MenuItem(self.file_mnu, wx.ID_ANY, 
            text=u"Open CSV\tCTRL+O", help="Opens a CSV file")
        self.file_mnu.AppendItem(self.open_file_mnui)
        self.Bind(wx.EVT_MENU, self.on_openfile, id=self.open_file_mnui.GetId())
        self.save_file_mnui = wx.MenuItem(self.file_mnu, wx.ID_ANY,
            text=u"Save CSV\tCTRL+S", help="Saves the CSV file")
        self.file_mnu.AppendItem(self.save_file_mnui)
        self.Bind(wx.EVT_MENU, self.on_savefile, id=self.save_file_mnui.GetId())
        self.quit_mnui = wx.MenuItem(self.file_mnu, wx.ID_ANY,
            text=u"Exit Demo\tCTRL+X", help="Exits wxSpreadsheet Demo")
        self.file_mnu.AppendSeparator()
        self.file_mnu.AppendItem(self.quit_mnui)
        self.Bind(wx.EVT_MENU, self.on_quit, id=self.quit_mnui.GetId())
        self.menubar.Append(self.file_mnu, "&File")
        self.SetMenuBar(self.menubar)

    def init_ui(self):
        '''Creates and lays out the user interface'''
        self.main_panel = wx.Panel(self)
        self.main_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.statusbar = wx.StatusBar(self, -1)
        self.SetStatusBar(self.statusbar)
        self.spreadsheet = wxspreadsheet.Spreadsheet(self.main_panel)
        self.main_panel_sizer.Add(self.spreadsheet, 1, self.sizer_flags, self.widget_margin)

        self.main_panel.SetSizerAndFit(self.main_panel_sizer)

    # Event handlers
    def on_quit(self, evt):
        '''Handles the Quit event, confirms exit'''
        quit_dlg = wx.MessageDialog(self, 'Are you sure you want to quit?',
            'Exit Program?', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        if quit_dlg.ShowModal() == wx.ID_OK:
            self.Destroy()

    def on_openfile(self, evt):
        '''Handles the Open File event'''
        file_dlg = wx.FileDialog(self, message = "Please choose a CSV file to open",
            wildcard="CSV files (*.csv)|*.csv|All files (*.*)|*.*", style=wx.FD_OPEN)
        if file_dlg.ShowModal() == wx.ID_OK:
            self.spreadsheet.ReadCSV(file_dlg.GetPath())

    def on_savefile(self, evt):
        '''Handles the Save File event'''
        file_dlg = wx.FileDialog(self, message="Please choose a filename for saving",
            wildcard="CSV files (*.csv)|*.csv|All files (*.*)|*.*", style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        if file_dlg.ShowModal() == wx.ID_OK:
            self.spreadsheet.WriteCSV(file_dlg.GetPath())

def main():
    demo_app = wx.PySimpleApp()
    ui = wxSpreadSheetDemo(None)
    ui.Show(True)
    demo_app.MainLoop()

if __name__=="__main__":
    main()
