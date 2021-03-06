from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

import styles.styles as styles

import functions.tables.createTable as createTable
import functions.tables.importTable as importTable

import functions.buttons.navigation as navigation

from constants.screens import screens
class DelayInput(QMainWindow):
    def __init__(self, widget):
        
        super(DelayInput, self).__init__()
        
        #? load Ui file
        loadUi("src/screens/ui/DelayScreen.ui",self)
        
        #? Create a table with n jobs 
        createTable.delayTable(self, widget = widget)

        #? Handle navigation
        navigation.handleNavigation(self, widget = widget, screen = screens["DelayInput"])

        #? Initialize the state of next button
        self.continueButton.setStyleSheet(styles.continueButtonDisabled)
        self.continueButton.setEnabled(False)

        #? Initialize Errors
        self.errorExists = False

        #? Handle file import
        self.importButton.clicked.connect(lambda : importTable.delayTable(self, 2, 2, widget = widget))
        
        #? Track button updates
        self.matrixTable.itemChanged.connect(lambda : navigation.updateNextButton(self, widget = widget, screen = screens["DelayInput"]))