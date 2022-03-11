# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc
import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QSize(1280, 800))
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Montserrat\";\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #000000;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////"
                        "//\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushB"
                        "utton:pressed {	\n"
"	background-color: rgb(237, 28, 40);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggle"
                        "Button:pressed {\n"
"	background-color: rgb(237, 28, 40);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(0, 0, 0); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Conte"
                        "nt */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { backgroun"
                        "d-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color:"
                        " rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(237, 28, 40);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
" "
                        "   border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(237, 28, 40);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selectio"
                        "n-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(237, 28, 40);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(237, 28, 40);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-posit"
                        "ion: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(237, 28, 40);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(237, 28, 40);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius"
                        ": 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59,"
                        " 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox:"
                        ":drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-co"
                        "lor: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////"
                        "////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(237, 28, 40);\n"
"	font: 11pt \"Montserrat\";\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_32 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        self.titleLeftApp.setFont(font)
        self.titleLeftApp.setStyleSheet(u"font: 10pt \"Montserrat\";\n"
"color: rgb(255, 255, 255);")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        self.titleLeftDescription.setFont(font)
        self.titleLeftDescription.setStyleSheet(u"font: 10pt \"Montserrat\";\n"
"color: rgb(237, 28, 40);")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_5 = QLabel(self.topLogoInfo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 40, 40))
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setStyleSheet(u"image: url(:/logo/LogoRESILIENCE4.png);")

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setEnabled(False)
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"font: 10pt \"Montserrat\";")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btnRegistrarUsuario = QPushButton(self.topMenu)
        self.btnRegistrarUsuario.setObjectName(u"btnRegistrarUsuario")
        sizePolicy.setHeightForWidth(self.btnRegistrarUsuario.sizePolicy().hasHeightForWidth())
        self.btnRegistrarUsuario.setSizePolicy(sizePolicy)
        self.btnRegistrarUsuario.setMinimumSize(QSize(0, 45))
        self.btnRegistrarUsuario.setFont(font)
        self.btnRegistrarUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegistrarUsuario.setLayoutDirection(Qt.LeftToRight)
        self.btnRegistrarUsuario.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user-follow.png);\n"
"font: 10pt \"Montserrat\";\n"
"")

        self.verticalLayout_8.addWidget(self.btnRegistrarUsuario)

        self.btnReservaClase = QPushButton(self.topMenu)
        self.btnReservaClase.setObjectName(u"btnReservaClase")
        sizePolicy.setHeightForWidth(self.btnReservaClase.sizePolicy().hasHeightForWidth())
        self.btnReservaClase.setSizePolicy(sizePolicy)
        self.btnReservaClase.setMinimumSize(QSize(0, 45))
        self.btnReservaClase.setFont(font)
        self.btnReservaClase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnReservaClase.setLayoutDirection(Qt.LeftToRight)
        self.btnReservaClase.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-calendar-check.png);\n"
"font: 10pt \"Montserrat\";")

        self.verticalLayout_8.addWidget(self.btnReservaClase)

        self.btnBuscarUsuario = QPushButton(self.topMenu)
        self.btnBuscarUsuario.setObjectName(u"btnBuscarUsuario")
        sizePolicy.setHeightForWidth(self.btnBuscarUsuario.sizePolicy().hasHeightForWidth())
        self.btnBuscarUsuario.setSizePolicy(sizePolicy)
        self.btnBuscarUsuario.setMinimumSize(QSize(0, 45))
        self.btnBuscarUsuario.setFont(font)
        self.btnBuscarUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBuscarUsuario.setLayoutDirection(Qt.LeftToRight)
        self.btnBuscarUsuario.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);\n"
"font: 10pt \"Montserrat\";")

        self.verticalLayout_8.addWidget(self.btnBuscarUsuario)

        self.btnRegistrarEmpleado = QPushButton(self.topMenu)
        self.btnRegistrarEmpleado.setObjectName(u"btnRegistrarEmpleado")
        sizePolicy.setHeightForWidth(self.btnRegistrarEmpleado.sizePolicy().hasHeightForWidth())
        self.btnRegistrarEmpleado.setSizePolicy(sizePolicy)
        self.btnRegistrarEmpleado.setMinimumSize(QSize(0, 45))
        self.btnRegistrarEmpleado.setFont(font)
        self.btnRegistrarEmpleado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegistrarEmpleado.setLayoutDirection(Qt.LeftToRight)
        self.btnRegistrarEmpleado.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);\n"
"font: 10pt \"Montserrat\";")

        self.verticalLayout_8.addWidget(self.btnRegistrarEmpleado)

        self.btnNuevaSesion = QPushButton(self.topMenu)
        self.btnNuevaSesion.setObjectName(u"btnNuevaSesion")
        sizePolicy.setHeightForWidth(self.btnNuevaSesion.sizePolicy().hasHeightForWidth())
        self.btnNuevaSesion.setSizePolicy(sizePolicy)
        self.btnNuevaSesion.setMinimumSize(QSize(0, 45))
        self.btnNuevaSesion.setFont(font)
        self.btnNuevaSesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevaSesion.setLayoutDirection(Qt.LeftToRight)
        self.btnNuevaSesion.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clipboard.png);\n"
"font: 10pt \"Montserrat\";")

        self.verticalLayout_8.addWidget(self.btnNuevaSesion)

        self.btnNotificacion = QPushButton(self.topMenu)
        self.btnNotificacion.setObjectName(u"btnNotificacion")
        sizePolicy.setHeightForWidth(self.btnNotificacion.sizePolicy().hasHeightForWidth())
        self.btnNotificacion.setSizePolicy(sizePolicy)
        self.btnNotificacion.setMinimumSize(QSize(0, 45))
        self.btnNotificacion.setFont(font)
        self.btnNotificacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNotificacion.setLayoutDirection(Qt.LeftToRight)
        self.btnNotificacion.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-mobile.png);\n"
"font: 10pt \"Montserrat\";")

        self.verticalLayout_8.addWidget(self.btnNotificacion)

        self.btnAtras = QPushButton(self.topMenu)
        self.btnAtras.setObjectName(u"btnAtras")
        sizePolicy.setHeightForWidth(self.btnAtras.sizePolicy().hasHeightForWidth())
        self.btnAtras.setSizePolicy(sizePolicy)
        self.btnAtras.setMinimumSize(QSize(0, 45))
        self.btnAtras.setFont(font)
        self.btnAtras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAtras.setLayoutDirection(Qt.LeftToRight)
        self.btnAtras.setStyleSheet(u"font: 10pt \"Montserrat\";\n"
"background-image: url(:/icons/images/icons/cil-arrow-left.png);")

        self.verticalLayout_8.addWidget(self.btnAtras)

        self.btnCerrarSesion = QPushButton(self.topMenu)
        self.btnCerrarSesion.setObjectName(u"btnCerrarSesion")
        sizePolicy.setHeightForWidth(self.btnCerrarSesion.sizePolicy().hasHeightForWidth())
        self.btnCerrarSesion.setSizePolicy(sizePolicy)
        self.btnCerrarSesion.setMinimumSize(QSize(0, 45))
        self.btnCerrarSesion.setFont(font)
        self.btnCerrarSesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCerrarSesion.setLayoutDirection(Qt.LeftToRight)
        self.btnCerrarSesion.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-exit-to-app.png);\n"
"font: 10pt \"Montserrat\";")

        self.verticalLayout_8.addWidget(self.btnCerrarSesion)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setStyleSheet(u"font: 13pt \"Montserrat\";\n"
"color: rgb(255, 255, 255);")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamily(u"Montserrat")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy3)
        self.content.setMinimumSize(QSize(1235, 735))
        self.content.setLayoutDirection(Qt.LeftToRight)
        self.content.setAutoFillBackground(False)
        self.content.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        sizePolicy3.setHeightForWidth(self.pagesContainer.sizePolicy().hasHeightForWidth())
        self.pagesContainer.setSizePolicy(sizePolicy3)
        self.pagesContainer.setAutoFillBackground(False)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
"")
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.lytReservar = QWidget()
        self.lytReservar.setObjectName(u"lytReservar")
        self.lytReservar.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(237, 28, 40);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	image: url(:/images/flecha-hacia-abajo.png);\n"
""
                        "	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(237, 28, 40);\n"
"	font: 12pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(238, 56, 67);\n"
"	border: 2px solid rgb(238, 56, 67);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(237, 28, 40);\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}")
        self.verticalLayout_23 = QVBoxLayout(self.lytReservar)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 20, -1, 20)
        self.lblLogoReservar = QLabel(self.lytReservar)
        self.lblLogoReservar.setObjectName(u"lblLogoReservar")
        self.lblLogoReservar.setMinimumSize(QSize(500, 100))
        self.lblLogoReservar.setMaximumSize(QSize(500, 100))
        self.lblLogoReservar.setStyleSheet(u"image: url(:/images/images/images/LogoRESILIENCE2.png);")

        self.horizontalLayout_12.addWidget(self.lblLogoReservar)


        self.verticalLayout_23.addLayout(self.horizontalLayout_12)

        self.verticalFrame = QFrame(self.lytReservar)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_18 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_div_content_2 = QFrame(self.verticalFrame)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txtNumCliente = QLineEdit(self.frame_content_wid_2)
        self.txtNumCliente.setObjectName(u"txtNumCliente")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txtNumCliente.sizePolicy().hasHeightForWidth())
        self.txtNumCliente.setSizePolicy(sizePolicy4)
        self.txtNumCliente.setMinimumSize(QSize(0, 45))
        self.txtNumCliente.setMaximumSize(QSize(425, 45))
        self.txtNumCliente.setStyleSheet(u"")
        self.txtNumCliente.setMaxLength(4)

        self.gridLayout_2.addWidget(self.txtNumCliente, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_content_wid_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.frame_content_wid_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 1)

        self.lblNumCliente = QLabel(self.frame_content_wid_2)
        self.lblNumCliente.setObjectName(u"lblNumCliente")
        self.lblNumCliente.setMinimumSize(QSize(0, 45))
        self.lblNumCliente.setMaximumSize(QSize(425, 45))

        self.gridLayout_2.addWidget(self.lblNumCliente, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_content_wid_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_2)


        self.verticalLayout_24.addWidget(self.frame_content_wid_2)


        self.verticalLayout_18.addWidget(self.frame_div_content_2)


        self.verticalLayout_23.addWidget(self.verticalFrame)

        self.verticalFrame1 = QFrame(self.lytReservar)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalFrame1.setMinimumSize(QSize(0, 150))
        self.row_8 = QVBoxLayout(self.verticalFrame1)
        self.row_8.setSpacing(6)
        self.row_8.setObjectName(u"row_8")
        self.row_8.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 100)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(50)
        self.gridLayout_4.setContentsMargins(30, -1, -1, -1)
        self.cmbHorario = QComboBox(self.verticalFrame1)
        self.cmbHorario.setObjectName(u"cmbHorario")
        sizePolicy4.setHeightForWidth(self.cmbHorario.sizePolicy().hasHeightForWidth())
        self.cmbHorario.setSizePolicy(sizePolicy4)
        self.cmbHorario.setMinimumSize(QSize(0, 45))
        self.cmbHorario.setMaximumSize(QSize(425, 45))
        self.cmbHorario.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbHorario.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.cmbHorario, 0, 0, 1, 1)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.btnReservarClase = QPushButton(self.verticalFrame1)
        self.btnReservarClase.setObjectName(u"btnReservarClase")
        self.btnReservarClase.setMinimumSize(QSize(200, 35))
        self.btnReservarClase.setMaximumSize(QSize(200, 35))
        self.btnReservarClase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnReservarClase.setStyleSheet(u"")

        self.horizontalLayout_28.addWidget(self.btnReservarClase)


        self.gridLayout_4.addLayout(self.horizontalLayout_28, 2, 0, 1, 1)

        self.cmbClase = QComboBox(self.verticalFrame1)
        self.cmbClase.setObjectName(u"cmbClase")
        sizePolicy4.setHeightForWidth(self.cmbClase.sizePolicy().hasHeightForWidth())
        self.cmbClase.setSizePolicy(sizePolicy4)
        self.cmbClase.setMinimumSize(QSize(0, 45))
        self.cmbClase.setMaximumSize(QSize(425, 45))
        self.cmbClase.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbClase.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: rgb(100, 100,100 );")

        self.gridLayout_4.addWidget(self.cmbClase, 1, 0, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_4)

        self.calendarWidget = QCalendarWidget(self.verticalFrame1)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy5)
        self.calendarWidget.setMinimumSize(QSize(0, 325))
        self.calendarWidget.setMaximumSize(QSize(600, 325))
        self.calendarWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.calendarWidget.setStyleSheet(u"color: rgb(100, 100, 100);\n"
"font: 12pt \"Montserrat\";\n"
"background-color: rgb(220, 220, 220);\n"
"alternate-background-color: rgb(174, 174, 174);\n"
"selection-background-color: rgb(237, 28, 40);")
        self.calendarWidget.setSelectedDate(QDate(2021, 8, 2))
        self.calendarWidget.setMinimumDate(QDate(2021, 8, 2))
        self.calendarWidget.setFirstDayOfWeek(Qt.Monday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setDateEditAcceptDelay(1500)

        self.horizontalLayout_8.addWidget(self.calendarWidget)


        self.row_8.addLayout(self.horizontalLayout_8)


        self.verticalLayout_23.addWidget(self.verticalFrame1)

        self.stackedWidget.addWidget(self.lytReservar)
        self.lytBuscarUsuario = QWidget()
        self.lytBuscarUsuario.setObjectName(u"lytBuscarUsuario")
        self.lytBuscarUsuario.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(237, 28, 40);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	image: url(:/images/flecha-hacia-abajo.png);\n"
""
                        "	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	color: #000000;\n"
"    border: transparent;\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 1px;\n"
"    border-top-right-radius: 1px;\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(237, 28, 40);\n"
"	font: 12pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(238, 56, 67);\n"
"	border: 2px solid rgb(238, 56, 67);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(237, 28, 40);\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.lytBuscarUsuario)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.lblFotoPerfil = QLabel(self.lytBuscarUsuario)
        self.lblFotoPerfil.setObjectName(u"lblFotoPerfil")
        self.lblFotoPerfil.setMinimumSize(QSize(100, 80))
        self.lblFotoPerfil.setMaximumSize(QSize(100, 80))
        self.lblFotoPerfil.setStyleSheet(u"image: url(:/logo/foto_perfil.png);")
        self.lblFotoPerfil.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.lblFotoPerfil)

        self.lblLogoBuscar = QLabel(self.lytBuscarUsuario)
        self.lblLogoBuscar.setObjectName(u"lblLogoBuscar")
        self.lblLogoBuscar.setMinimumSize(QSize(500, 100))
        self.lblLogoBuscar.setMaximumSize(QSize(500, 100))
        self.lblLogoBuscar.setStyleSheet(u"image: url(:/images/images/images/LogoRESILIENCE2.png);")

        self.horizontalLayout_29.addWidget(self.lblLogoBuscar)


        self.verticalLayout.addLayout(self.horizontalLayout_29)

        self.row_1 = QFrame(self.lytBuscarUsuario)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lblBuscar = QLabel(self.frame_content_wid_1)
        self.lblBuscar.setObjectName(u"lblBuscar")
        self.lblBuscar.setMinimumSize(QSize(425, 30))
        self.lblBuscar.setMaximumSize(QSize(900, 30))

        self.gridLayout.addWidget(self.lblBuscar, 1, 0, 1, 2)

        self.cmbOpcionRenovar = QComboBox(self.frame_content_wid_1)
        self.cmbOpcionRenovar.setObjectName(u"cmbOpcionRenovar")
        self.cmbOpcionRenovar.setEnabled(False)
        sizePolicy.setHeightForWidth(self.cmbOpcionRenovar.sizePolicy().hasHeightForWidth())
        self.cmbOpcionRenovar.setSizePolicy(sizePolicy)
        self.cmbOpcionRenovar.setMinimumSize(QSize(0, 35))
        self.cmbOpcionRenovar.setMaximumSize(QSize(425, 35))
        self.cmbOpcionRenovar.setBaseSize(QSize(0, 0))
        self.cmbOpcionRenovar.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbOpcionRenovar.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: rgb(100, 100,100 );")
        self.cmbOpcionRenovar.setMaxVisibleItems(10)

        self.gridLayout.addWidget(self.cmbOpcionRenovar, 3, 2, 1, 1)

        self.lbluid = QLineEdit(self.frame_content_wid_1)
        self.lbluid.setObjectName(u"lbluid")
        self.lbluid.setEnabled(False)
        self.lbluid.setMinimumSize(QSize(150, 30))
        self.lbluid.setMaximumSize(QSize(150, 30))
        self.lbluid.setStyleSheet(u"border-color: transparent;\n"
"color: transparent;\n"
"background-color: transparent;")

        self.gridLayout.addWidget(self.lbluid, 1, 3, 1, 1)

        self.btnBuscar = QPushButton(self.frame_content_wid_1)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setMinimumSize(QSize(0, 35))
        self.btnBuscar.setMaximumSize(QSize(200, 35))
        font3 = QFont()
        font3.setFamily(u"Montserrat")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.btnBuscar.setFont(font3)
        self.btnBuscar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBuscar.setAutoFillBackground(False)
        self.btnBuscar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnBuscar, 0, 3, 1, 1)

        self.lblOpcionRenovar = QLabel(self.frame_content_wid_1)
        self.lblOpcionRenovar.setObjectName(u"lblOpcionRenovar")
        self.lblOpcionRenovar.setMinimumSize(QSize(0, 30))
        self.lblOpcionRenovar.setMaximumSize(QSize(365, 30))
        self.lblOpcionRenovar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lblOpcionRenovar, 3, 1, 1, 1)

        self.chkOpcionRenovar = QCheckBox(self.frame_content_wid_1)
        self.chkOpcionRenovar.setObjectName(u"chkOpcionRenovar")
        sizePolicy.setHeightForWidth(self.chkOpcionRenovar.sizePolicy().hasHeightForWidth())
        self.chkOpcionRenovar.setSizePolicy(sizePolicy)
        self.chkOpcionRenovar.setMinimumSize(QSize(0, 30))
        self.chkOpcionRenovar.setMaximumSize(QSize(60, 30))
        self.chkOpcionRenovar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.chkOpcionRenovar, 3, 0, 1, 1)

        self.btnRenovar = QPushButton(self.frame_content_wid_1)
        self.btnRenovar.setObjectName(u"btnRenovar")
        self.btnRenovar.setEnabled(False)
        self.btnRenovar.setMinimumSize(QSize(0, 35))
        self.btnRenovar.setMaximumSize(QSize(200, 35))
        self.btnRenovar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRenovar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnRenovar, 3, 3, 1, 1)

        self.txtBuscar = QLineEdit(self.frame_content_wid_1)
        self.txtBuscar.setObjectName(u"txtBuscar")
        self.txtBuscar.setMinimumSize(QSize(425, 35))
        self.txtBuscar.setMaximumSize(QSize(900, 35))
        self.txtBuscar.setStyleSheet(u"")
        self.txtBuscar.setMaxLength(4)

        self.gridLayout.addWidget(self.txtBuscar, 0, 0, 1, 3)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.lytBuscarUsuario)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.row_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_11.addWidget(self.label)

        self.tableWidget = QTableWidget(self.row_2)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        font4 = QFont()
        font4.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 14):
            self.tableWidget.setRowCount(14)
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem15)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        font6 = QFont()
        font6.setFamily(u"Montserrat")
        font6.setPointSize(12)
        font6.setBold(False)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font6);
        __qtablewidgetitem16.setForeground(brush);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem16)
        font7 = QFont()
        font7.setPointSize(10)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font7);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem17)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font6);
        __qtablewidgetitem18.setForeground(brush1);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font7);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font6);
        __qtablewidgetitem20.setForeground(brush2);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font7);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem21)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font6);
        __qtablewidgetitem22.setForeground(brush3);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font7);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem23)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font6);
        __qtablewidgetitem24.setForeground(brush4);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font7);
        self.tableWidget.setItem(4, 1, __qtablewidgetitem25)
        brush5 = QBrush(QColor(52, 59, 72, 255))
        brush5.setStyle(Qt.NoBrush)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font6);
        __qtablewidgetitem26.setForeground(brush5);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font7);
        self.tableWidget.setItem(5, 1, __qtablewidgetitem27)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font6);
        __qtablewidgetitem28.setForeground(brush6);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font7);
        self.tableWidget.setItem(6, 1, __qtablewidgetitem29)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font6);
        __qtablewidgetitem30.setForeground(brush7);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font7);
        self.tableWidget.setItem(7, 1, __qtablewidgetitem31)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font6);
        __qtablewidgetitem32.setForeground(brush8);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font7);
        self.tableWidget.setItem(8, 1, __qtablewidgetitem33)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font6);
        __qtablewidgetitem34.setForeground(brush9);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem34)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font6);
        __qtablewidgetitem35.setForeground(brush10);
        self.tableWidget.setItem(10, 0, __qtablewidgetitem35)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font6);
        __qtablewidgetitem36.setBackground(brush12);
        __qtablewidgetitem36.setForeground(brush11);
        self.tableWidget.setItem(11, 0, __qtablewidgetitem36)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font6);
        __qtablewidgetitem37.setForeground(brush13);
        self.tableWidget.setItem(12, 0, __qtablewidgetitem37)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font6);
        __qtablewidgetitem38.setForeground(brush14);
        self.tableWidget.setItem(13, 0, __qtablewidgetitem38)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy5)
        self.tableWidget.setMinimumSize(QSize(480, 445))
        self.tableWidget.setMaximumSize(QSize(480, 500))
        palette = QPalette()
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        brush16 = QBrush(QColor(0, 0, 0, 0))
        brush16.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush15)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette.setBrush(QPalette.Active, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush15)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush18)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        brush19 = QBrush(QColor(0, 0, 0, 255))
        brush19.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"gridline-color: transparent;\n"
"font: 10pt \"Montserrat\";\n"
"\n"
"\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_11.addWidget(self.tableWidget)

        self.tableWidget_2 = QTableWidget(self.row_2)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem39.setFont(font6);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        font8 = QFont()
        font8.setFamily(u"Montserrat")
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setKerning(True)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem40.setFont(font8);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem41.setFont(font6);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy5)
        self.tableWidget_2.setMinimumSize(QSize(0, 0))
        self.tableWidget_2.setMaximumSize(QSize(480, 445))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush15)
        brush20 = QBrush(QColor(0, 0, 0, 255))
        brush20.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush15)
        brush21 = QBrush(QColor(0, 0, 0, 255))
        brush21.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush21)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        brush22 = QBrush(QColor(0, 0, 0, 255))
        brush22.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush22)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.tableWidget_2.setPalette(palette1)
        self.tableWidget_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.tableWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_2.setStyleSheet(u"background-color: transparent;\n"
"gridline-color: transparent;\n"
"border-color: transparent;\n"
"font: 9pt \"Montserrat\";")
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setAutoScrollMargin(16)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setTabKeyNavigation(True)
        self.tableWidget_2.setProperty("showDropIndicator", True)
        self.tableWidget_2.setDragEnabled(False)
        self.tableWidget_2.setDragDropOverwriteMode(True)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget_2.setTextElideMode(Qt.ElideRight)
        self.tableWidget_2.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(150)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_11.addWidget(self.tableWidget_2)

        self.label_2 = QLabel(self.row_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_11.addWidget(self.label_2)


        self.verticalLayout_19.addLayout(self.horizontalLayout_11)


        self.verticalLayout.addWidget(self.row_2)

        self.stackedWidget.addWidget(self.lytBuscarUsuario)
        self.lytEmpleado = QWidget()
        self.lytEmpleado.setObjectName(u"lytEmpleado")
        self.lytEmpleado.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(237, 28, 40);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	image: url(:/images/flecha-hacia-abajo.png);\n"
""
                        "	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(237, 28, 40);\n"
"	font: 12pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(238, 56, 67);\n"
"	border: 2px solid rgb(238, 56, 67);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(237, 28, 40);\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}")
        self.verticalLayout_41 = QVBoxLayout(self.lytEmpleado)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(-1, 20, -1, 20)
        self.lblLogoRegistro_2 = QLabel(self.lytEmpleado)
        self.lblLogoRegistro_2.setObjectName(u"lblLogoRegistro_2")
        self.lblLogoRegistro_2.setMinimumSize(QSize(0, 140))
        self.lblLogoRegistro_2.setMaximumSize(QSize(400, 140))
        self.lblLogoRegistro_2.setStyleSheet(u"image: url(:/images/IMAGOTIPO.png);")
        self.lblLogoRegistro_2.setScaledContents(False)

        self.horizontalLayout_48.addWidget(self.lblLogoRegistro_2)


        self.verticalLayout_41.addLayout(self.horizontalLayout_48)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_25 = QLabel(self.lytEmpleado)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(70, 30))
        self.label_25.setMaximumSize(QSize(70, 30))
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_25)

        self.txtNombreEmpleado = QLineEdit(self.lytEmpleado)
        self.txtNombreEmpleado.setObjectName(u"txtNombreEmpleado")
        sizePolicy4.setHeightForWidth(self.txtNombreEmpleado.sizePolicy().hasHeightForWidth())
        self.txtNombreEmpleado.setSizePolicy(sizePolicy4)
        self.txtNombreEmpleado.setMinimumSize(QSize(450, 45))
        self.txtNombreEmpleado.setMaximumSize(QSize(450, 45))
        self.txtNombreEmpleado.setMaxLength(100)
        self.txtNombreEmpleado.setEchoMode(QLineEdit.Normal)
        self.txtNombreEmpleado.setDragEnabled(False)
        self.txtNombreEmpleado.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txtNombreEmpleado.setClearButtonEnabled(True)

        self.horizontalLayout_30.addWidget(self.txtNombreEmpleado)

        self.label_26 = QLabel(self.lytEmpleado)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(70, 30))
        self.label_26.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_30.addWidget(self.label_26)


        self.verticalLayout_34.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.lblNombre_2 = QLabel(self.lytEmpleado)
        self.lblNombre_2.setObjectName(u"lblNombre_2")
        self.lblNombre_2.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_33.addWidget(self.lblNombre_2)


        self.verticalLayout_34.addLayout(self.horizontalLayout_33)


        self.verticalLayout_33.addLayout(self.verticalLayout_34)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_46 = QLabel(self.lytEmpleado)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(70, 30))
        self.label_46.setMaximumSize(QSize(70, 30))
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.label_46)

        self.txtApellidoEmpleado = QLineEdit(self.lytEmpleado)
        self.txtApellidoEmpleado.setObjectName(u"txtApellidoEmpleado")
        sizePolicy4.setHeightForWidth(self.txtApellidoEmpleado.sizePolicy().hasHeightForWidth())
        self.txtApellidoEmpleado.setSizePolicy(sizePolicy4)
        self.txtApellidoEmpleado.setMinimumSize(QSize(450, 45))
        self.txtApellidoEmpleado.setMaximumSize(QSize(450, 45))
        self.txtApellidoEmpleado.setMaxLength(100)
        self.txtApellidoEmpleado.setDragEnabled(False)
        self.txtApellidoEmpleado.setClearButtonEnabled(True)

        self.horizontalLayout_34.addWidget(self.txtApellidoEmpleado)

        self.label_47 = QLabel(self.lytEmpleado)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(70, 30))
        self.label_47.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_34.addWidget(self.label_47)


        self.verticalLayout_35.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.lblApellido_2 = QLabel(self.lytEmpleado)
        self.lblApellido_2.setObjectName(u"lblApellido_2")
        self.lblApellido_2.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_35.addWidget(self.lblApellido_2)


        self.verticalLayout_35.addLayout(self.horizontalLayout_35)


        self.verticalLayout_33.addLayout(self.verticalLayout_35)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_7 = QLabel(self.lytEmpleado)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(70, 30))
        self.label_7.setMaximumSize(QSize(70, 30))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_7)

        self.cmbTipoEmpleado = QComboBox(self.lytEmpleado)
        self.cmbTipoEmpleado.addItem("")
        self.cmbTipoEmpleado.addItem("")
        self.cmbTipoEmpleado.addItem("")
        self.cmbTipoEmpleado.setObjectName(u"cmbTipoEmpleado")
        self.cmbTipoEmpleado.setMinimumSize(QSize(450, 45))
        self.cmbTipoEmpleado.setMaximumSize(QSize(450, 45))
        self.cmbTipoEmpleado.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbTipoEmpleado.setMaxVisibleItems(3)

        self.horizontalLayout_36.addWidget(self.cmbTipoEmpleado)

        self.label_27 = QLabel(self.lytEmpleado)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(70, 30))
        self.label_27.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_36.addWidget(self.label_27)


        self.verticalLayout_36.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.lblCorreo_2 = QLabel(self.lytEmpleado)
        self.lblCorreo_2.setObjectName(u"lblCorreo_2")
        self.lblCorreo_2.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_37.addWidget(self.lblCorreo_2)


        self.verticalLayout_36.addLayout(self.horizontalLayout_37)


        self.verticalLayout_33.addLayout(self.verticalLayout_36)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_31 = QLabel(self.lytEmpleado)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(70, 30))
        self.label_31.setMaximumSize(QSize(70, 30))
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_31)

        self.txtContrasenaEmpleado = QLineEdit(self.lytEmpleado)
        self.txtContrasenaEmpleado.setObjectName(u"txtContrasenaEmpleado")
        sizePolicy4.setHeightForWidth(self.txtContrasenaEmpleado.sizePolicy().hasHeightForWidth())
        self.txtContrasenaEmpleado.setSizePolicy(sizePolicy4)
        self.txtContrasenaEmpleado.setMinimumSize(QSize(450, 45))
        self.txtContrasenaEmpleado.setMaximumSize(QSize(450, 45))
        self.txtContrasenaEmpleado.setMaxLength(100)
        self.txtContrasenaEmpleado.setEchoMode(QLineEdit.Password)
        self.txtContrasenaEmpleado.setClearButtonEnabled(True)

        self.horizontalLayout_38.addWidget(self.txtContrasenaEmpleado)

        self.label_28 = QLabel(self.lytEmpleado)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(70, 30))
        self.label_28.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_38.addWidget(self.label_28)


        self.verticalLayout_37.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.lblTelefono_2 = QLabel(self.lytEmpleado)
        self.lblTelefono_2.setObjectName(u"lblTelefono_2")
        self.lblTelefono_2.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_39.addWidget(self.lblTelefono_2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_39)


        self.verticalLayout_33.addLayout(self.verticalLayout_37)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_32 = QLabel(self.lytEmpleado)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(70, 30))
        self.label_32.setMaximumSize(QSize(70, 30))
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_32)

        self.txtRepetirContrasena = QLineEdit(self.lytEmpleado)
        self.txtRepetirContrasena.setObjectName(u"txtRepetirContrasena")
        sizePolicy4.setHeightForWidth(self.txtRepetirContrasena.sizePolicy().hasHeightForWidth())
        self.txtRepetirContrasena.setSizePolicy(sizePolicy4)
        self.txtRepetirContrasena.setMinimumSize(QSize(450, 45))
        self.txtRepetirContrasena.setMaximumSize(QSize(450, 45))
        self.txtRepetirContrasena.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhPreferNumbers|Qt.ImhSensitiveData)
        self.txtRepetirContrasena.setMaxLength(100)
        self.txtRepetirContrasena.setEchoMode(QLineEdit.Password)
        self.txtRepetirContrasena.setClearButtonEnabled(True)

        self.horizontalLayout_40.addWidget(self.txtRepetirContrasena)

        self.label_33 = QLabel(self.lytEmpleado)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(70, 30))
        self.label_33.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_40.addWidget(self.label_33)


        self.verticalLayout_38.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.lblEdad_2 = QLabel(self.lytEmpleado)
        self.lblEdad_2.setObjectName(u"lblEdad_2")
        self.lblEdad_2.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_41.addWidget(self.lblEdad_2)


        self.verticalLayout_38.addLayout(self.horizontalLayout_41)


        self.verticalLayout_33.addLayout(self.verticalLayout_38)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_56 = QLabel(self.lytEmpleado)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(70, 30))
        self.label_56.setMaximumSize(QSize(70, 30))
        self.label_56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.label_56)

        self.label_57 = QLabel(self.lytEmpleado)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(70, 30))
        self.label_57.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_42.addWidget(self.label_57)


        self.verticalLayout_39.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.lblTipoMembresia_2 = QLabel(self.lytEmpleado)
        self.lblTipoMembresia_2.setObjectName(u"lblTipoMembresia_2")
        self.lblTipoMembresia_2.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_43.addWidget(self.lblTipoMembresia_2)


        self.verticalLayout_39.addLayout(self.horizontalLayout_43)


        self.verticalLayout_33.addLayout(self.verticalLayout_39)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.btnRegistroEmpleado = QPushButton(self.lytEmpleado)
        self.btnRegistroEmpleado.setObjectName(u"btnRegistroEmpleado")
        self.btnRegistroEmpleado.setMinimumSize(QSize(0, 35))
        self.btnRegistroEmpleado.setMaximumSize(QSize(200, 35))
        self.btnRegistroEmpleado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegistroEmpleado.setStyleSheet(u"")

        self.horizontalLayout_44.addWidget(self.btnRegistroEmpleado)


        self.verticalLayout_33.addLayout(self.horizontalLayout_44)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.lblRegistrarEmpleado = QLabel(self.lytEmpleado)
        self.lblRegistrarEmpleado.setObjectName(u"lblRegistrarEmpleado")
        self.lblRegistrarEmpleado.setMaximumSize(QSize(400, 30))
        self.lblRegistrarEmpleado.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.lblRegistrarEmpleado)


        self.verticalLayout_40.addLayout(self.horizontalLayout_45)


        self.verticalLayout_33.addLayout(self.verticalLayout_40)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")

        self.verticalLayout_33.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.lblGuardar_2 = QLabel(self.lytEmpleado)
        self.lblGuardar_2.setObjectName(u"lblGuardar_2")
        self.lblGuardar_2.setMaximumSize(QSize(400, 30))
        self.lblGuardar_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.lblGuardar_2)


        self.verticalLayout_33.addLayout(self.horizontalLayout_47)


        self.verticalLayout_41.addLayout(self.verticalLayout_33)

        self.stackedWidget.addWidget(self.lytEmpleado)
        self.lytNuevaClase = QWidget()
        self.lytNuevaClase.setObjectName(u"lytNuevaClase")
        self.lytNuevaClase.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(237, 28, 40);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	image: url(:/images/flecha-hacia-abajo.png);\n"
"	"
                        "background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(237, 28, 40);\n"
"	font: 12pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(238, 56, 67);\n"
"	border: 2px solid rgb(238, 56, 67);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(237, 28, 40);\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"	color: #000000;\n"
"    border: transparent;\n"
"	background-color: #ffffff;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"	font: 11pt \"Montserrat\";\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	color: #000000;\n"
""
                        "    border: transparent;\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 1px;\n"
"    border-top-right-radius: 1px;\n"
"	font: 11pt \"Montserrat\";\n"
"}")
        self.verticalLayout_42 = QVBoxLayout(self.lytNuevaClase)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(-1, 30, -1, 30)
        self.lblLogoReservar_2 = QLabel(self.lytNuevaClase)
        self.lblLogoReservar_2.setObjectName(u"lblLogoReservar_2")
        self.lblLogoReservar_2.setMinimumSize(QSize(500, 100))
        self.lblLogoReservar_2.setMaximumSize(QSize(500, 100))
        self.lblLogoReservar_2.setStyleSheet(u"image: url(:/images/images/images/LogoRESILIENCE2.png);")

        self.horizontalLayout_49.addWidget(self.lblLogoReservar_2)


        self.verticalLayout_42.addLayout(self.horizontalLayout_49)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(50)
        self.gridLayout_6.setVerticalSpacing(25)
        self.gridLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.lytNuevaClase)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)

        self.lblNuevaAgregar = QLabel(self.lytNuevaClase)
        self.lblNuevaAgregar.setObjectName(u"lblNuevaAgregar")
        self.lblNuevaAgregar.setMinimumSize(QSize(50, 25))
        self.lblNuevaAgregar.setMaximumSize(QSize(250, 25))

        self.gridLayout_6.addWidget(self.lblNuevaAgregar, 5, 3, 1, 1)

        self.btnAgregar_2 = QPushButton(self.lytNuevaClase)
        self.btnAgregar_2.setObjectName(u"btnAgregar_2")
        self.btnAgregar_2.setMinimumSize(QSize(40, 40))
        self.btnAgregar_2.setMaximumSize(QSize(40, 40))
        self.btnAgregar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregar_2.setStyleSheet(u"image: url(:/icons/images/icons/cil-plus.png);")

        self.gridLayout_6.addWidget(self.btnAgregar_2, 0, 4, 1, 1)

        self.lblHora1 = QLabel(self.lytNuevaClase)
        self.lblHora1.setObjectName(u"lblHora1")
        self.lblHora1.setMinimumSize(QSize(50, 25))
        self.lblHora1.setMaximumSize(QSize(50, 25))

        self.gridLayout_6.addWidget(self.lblHora1, 0, 5, 1, 1)

        self.label_11 = QLabel(self.lytNuevaClase)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(180, 15))
        self.label_11.setMaximumSize(QSize(180, 15))

        self.gridLayout_6.addWidget(self.label_11, 5, 2, 1, 1)

        self.lblHora2 = QLabel(self.lytNuevaClase)
        self.lblHora2.setObjectName(u"lblHora2")
        self.lblHora2.setMinimumSize(QSize(50, 25))
        self.lblHora2.setMaximumSize(QSize(50, 25))

        self.gridLayout_6.addWidget(self.lblHora2, 1, 5, 1, 1)

        self.lblFechaAgregar = QLabel(self.lytNuevaClase)
        self.lblFechaAgregar.setObjectName(u"lblFechaAgregar")
        self.lblFechaAgregar.setMinimumSize(QSize(0, 15))
        self.lblFechaAgregar.setMaximumSize(QSize(225, 15))

        self.gridLayout_6.addWidget(self.lblFechaAgregar, 1, 2, 1, 1)

        self.txtFechaAgregar = QLineEdit(self.lytNuevaClase)
        self.txtFechaAgregar.setObjectName(u"txtFechaAgregar")
        self.txtFechaAgregar.setMinimumSize(QSize(0, 40))
        self.txtFechaAgregar.setMaximumSize(QSize(300, 40))
        self.txtFechaAgregar.setStyleSheet(u"")
        self.txtFechaAgregar.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.txtFechaAgregar.setMaxLength(10)
        self.txtFechaAgregar.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txtFechaAgregar, 0, 2, 1, 1)

        self.txtHoraAgregar = QLineEdit(self.lytNuevaClase)
        self.txtHoraAgregar.setObjectName(u"txtHoraAgregar")
        self.txtHoraAgregar.setMinimumSize(QSize(0, 40))
        self.txtHoraAgregar.setMaximumSize(QSize(300, 40))
        self.txtHoraAgregar.setStyleSheet(u"")
        self.txtHoraAgregar.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.txtHoraAgregar.setMaxLength(5)
        self.txtHoraAgregar.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txtHoraAgregar, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.lytNuevaClase)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setMaximumSize(QSize(40, 40))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"image: url(:/images/trash (2).png);")

        self.gridLayout_6.addWidget(self.pushButton, 9, 4, 1, 1)

        self.lblNivel_2 = QLabel(self.lytNuevaClase)
        self.lblNivel_2.setObjectName(u"lblNivel_2")
        self.lblNivel_2.setMinimumSize(QSize(280, 15))
        self.lblNivel_2.setMaximumSize(QSize(300, 15))

        self.gridLayout_6.addWidget(self.lblNivel_2, 8, 1, 1, 1)

        self.tableWidget_6 = QTableWidget(self.lytNuevaClase)
        if (self.tableWidget_6.columnCount() < 5):
            self.tableWidget_6.setColumnCount(5)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem46)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setMinimumSize(QSize(0, 110))
        self.tableWidget_6.setMaximumSize(QSize(960, 16777215))
        self.tableWidget_6.setSizeIncrement(QSize(0, 0))
        self.tableWidget_6.setStyleSheet(u"background-color: transparent;\n"
"gridline-color: transparent;\n"
"border-color: transparent;\n"
"font: 10pt \"Montserrat\";")
        self.tableWidget_6.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.tableWidget_6.setAlternatingRowColors(True)
        self.tableWidget_6.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_6.horizontalHeader().setVisible(False)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tableWidget_6.verticalHeader().setStretchLastSection(False)

        self.gridLayout_6.addWidget(self.tableWidget_6, 9, 1, 1, 3)

        self.cmbNombreSesion = QComboBox(self.lytNuevaClase)
        self.cmbNombreSesion.setObjectName(u"cmbNombreSesion")
        sizePolicy.setHeightForWidth(self.cmbNombreSesion.sizePolicy().hasHeightForWidth())
        self.cmbNombreSesion.setSizePolicy(sizePolicy)
        self.cmbNombreSesion.setMinimumSize(QSize(0, 40))
        self.cmbNombreSesion.setMaximumSize(QSize(300, 40))
        self.cmbNombreSesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbNombreSesion.setStyleSheet(u"")
        self.cmbNombreSesion.setEditable(False)
        self.cmbNombreSesion.setMaxVisibleItems(10)
        self.cmbNombreSesion.setInsertPolicy(QComboBox.InsertAtBottom)
        self.cmbNombreSesion.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.cmbNombreSesion.setModelColumn(0)

        self.gridLayout_6.addWidget(self.cmbNombreSesion, 4, 2, 1, 1)

        self.lblHoraAgregar = QLabel(self.lytNuevaClase)
        self.lblHoraAgregar.setObjectName(u"lblHoraAgregar")
        self.lblHoraAgregar.setMinimumSize(QSize(0, 15))
        self.lblHoraAgregar.setMaximumSize(QSize(225, 15))

        self.gridLayout_6.addWidget(self.lblHoraAgregar, 1, 3, 1, 1)

        self.txtNuevaAgregar = QLineEdit(self.lytNuevaClase)
        self.txtNuevaAgregar.setObjectName(u"txtNuevaAgregar")
        self.txtNuevaAgregar.setEnabled(True)
        self.txtNuevaAgregar.setMinimumSize(QSize(0, 40))
        self.txtNuevaAgregar.setMaximumSize(QSize(300, 40))
        self.txtNuevaAgregar.setStyleSheet(u"")
        self.txtNuevaAgregar.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.txtNuevaAgregar.setMaxLength(100)
        self.txtNuevaAgregar.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txtNuevaAgregar, 4, 3, 1, 1)

        self.label_37 = QLabel(self.lytNuevaClase)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 0, 6, 1, 1)

        self.lblNivel = QLabel(self.lytNuevaClase)
        self.lblNivel.setObjectName(u"lblNivel")
        self.lblNivel.setMinimumSize(QSize(0, 15))
        self.lblNivel.setMaximumSize(QSize(225, 15))

        self.gridLayout_6.addWidget(self.lblNivel, 8, 2, 1, 1)

        self.lblHora3 = QLabel(self.lytNuevaClase)
        self.lblHora3.setObjectName(u"lblHora3")
        self.lblHora3.setMinimumSize(QSize(50, 25))
        self.lblHora3.setMaximumSize(QSize(50, 50))

        self.gridLayout_6.addWidget(self.lblHora3, 4, 5, 1, 1)

        self.lblHora4 = QLabel(self.lytNuevaClase)
        self.lblHora4.setObjectName(u"lblHora4")
        self.lblHora4.setMinimumSize(QSize(50, 25))
        self.lblHora4.setMaximumSize(QSize(50, 25))

        self.gridLayout_6.addWidget(self.lblHora4, 5, 5, 1, 1)

        self.btnNuevaClase = QPushButton(self.lytNuevaClase)
        self.btnNuevaClase.setObjectName(u"btnNuevaClase")
        self.btnNuevaClase.setMinimumSize(QSize(40, 40))
        self.btnNuevaClase.setMaximumSize(QSize(40, 40))
        self.btnNuevaClase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevaClase.setStyleSheet(u"image: url(:/icons/images/icons/cil-plus.png);")

        self.gridLayout_6.addWidget(self.btnNuevaClase, 4, 4, 1, 1)

        self.cmbselecNivel = QComboBox(self.lytNuevaClase)
        self.cmbselecNivel.setObjectName(u"cmbselecNivel")
        sizePolicy.setHeightForWidth(self.cmbselecNivel.sizePolicy().hasHeightForWidth())
        self.cmbselecNivel.setSizePolicy(sizePolicy)
        self.cmbselecNivel.setMinimumSize(QSize(0, 40))
        self.cmbselecNivel.setMaximumSize(QSize(300, 40))
        self.cmbselecNivel.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbselecNivel.setStyleSheet(u"")
        self.cmbselecNivel.setMaxVisibleItems(10)
        self.cmbselecNivel.setInsertPolicy(QComboBox.InsertAtBottom)
        self.cmbselecNivel.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.cmbselecNivel.setModelColumn(0)

        self.gridLayout_6.addWidget(self.cmbselecNivel, 0, 1, 1, 1)

        self.cmbIntensidad = QComboBox(self.lytNuevaClase)
        self.cmbIntensidad.setObjectName(u"cmbIntensidad")
        sizePolicy.setHeightForWidth(self.cmbIntensidad.sizePolicy().hasHeightForWidth())
        self.cmbIntensidad.setSizePolicy(sizePolicy)
        self.cmbIntensidad.setMinimumSize(QSize(0, 40))
        self.cmbIntensidad.setMaximumSize(QSize(300, 40))
        self.cmbIntensidad.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbIntensidad.setStyleSheet(u"")
        self.cmbIntensidad.setMaxVisibleItems(10)
        self.cmbIntensidad.setInsertPolicy(QComboBox.InsertAtBottom)
        self.cmbIntensidad.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.cmbIntensidad.setModelColumn(0)

        self.gridLayout_6.addWidget(self.cmbIntensidad, 4, 1, 1, 1)

        self.txtUrlAgregar = QLineEdit(self.lytNuevaClase)
        self.txtUrlAgregar.setObjectName(u"txtUrlAgregar")
        self.txtUrlAgregar.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.txtUrlAgregar.sizePolicy().hasHeightForWidth())
        self.txtUrlAgregar.setSizePolicy(sizePolicy6)
        self.txtUrlAgregar.setMinimumSize(QSize(0, 40))
        self.txtUrlAgregar.setMaximumSize(QSize(1000, 40))
        self.txtUrlAgregar.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: rgb(100, 100,100 );")
        self.txtUrlAgregar.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.txtUrlAgregar.setMaxLength(500)
        self.txtUrlAgregar.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txtUrlAgregar, 6, 1, 1, 3)

        self.btnSubirLink = QPushButton(self.lytNuevaClase)
        self.btnSubirLink.setObjectName(u"btnSubirLink")
        self.btnSubirLink.setMinimumSize(QSize(40, 40))
        self.btnSubirLink.setMaximumSize(QSize(40, 40))
        self.btnSubirLink.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSubirLink.setStyleSheet(u"image: url(:/icons/images/icons/cil-data-transfer-up.png);")

        self.gridLayout_6.addWidget(self.btnSubirLink, 6, 4, 1, 1)


        self.verticalLayout_42.addLayout(self.gridLayout_6)

        self.lblAgregar = QLabel(self.lytNuevaClase)
        self.lblAgregar.setObjectName(u"lblAgregar")
        self.lblAgregar.setMinimumSize(QSize(0, 15))
        self.lblAgregar.setMaximumSize(QSize(16777215, 15))
        self.lblAgregar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.lblAgregar)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.btnAgregar = QPushButton(self.lytNuevaClase)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setMinimumSize(QSize(0, 35))
        self.btnAgregar.setMaximumSize(QSize(200, 35))
        self.btnAgregar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregar.setStyleSheet(u"")

        self.horizontalLayout_50.addWidget(self.btnAgregar)


        self.verticalLayout_42.addLayout(self.horizontalLayout_50)

        self.stackedWidget.addWidget(self.lytNuevaClase)
        self.lytNutriologo = QWidget()
        self.lytNutriologo.setObjectName(u"lytNutriologo")
        self.lytNutriologo.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(237, 28, 40);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	image: url(:/images/flecha-hacia-abajo.png);\n"
""
                        "	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"	color: #000000;\n"
"    border: transparent;\n"
"	background-color: #ffffff;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"	font: 11pt \"Montserrat\";\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	color: #000000;\n"
"    border: transparent;\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 1px;\n"
"    border-top-right-radius: 1px;\n"
"	font: 11pt \"Montserrat\";\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(237, 28, 40);\n"
"	font: 12pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"#pagesContainer QPushButton:hover {\n"
"	backgro"
                        "und-color: rgb(238, 56, 67);\n"
"	border: 2px solid rgb(238, 56, 67);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(237, 28, 40);\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}")
        self.verticalLayout_43 = QVBoxLayout(self.lytNutriologo)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.row_3 = QFrame(self.lytNutriologo)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.row_3)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_3 = QFrame(self.row_3)
        self.frame_div_content_3.setObjectName(u"frame_div_content_3")
        self.frame_div_content_3.setMinimumSize(QSize(0, 110))
        self.frame_div_content_3.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_3.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_div_content_3)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_3 = QFrame(self.frame_div_content_3)
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_content_wid_3)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_39 = QLabel(self.frame_content_wid_3)
        self.label_39.setObjectName(u"label_39")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy7)
        self.label_39.setMinimumSize(QSize(0, 0))
        self.label_39.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_55.addWidget(self.label_39)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(20)
        self.gridLayout_13.setVerticalSpacing(0)
        self.gridLayout_13.setContentsMargins(-1, 30, -1, 0)
        self.txtNClienteNut = QLineEdit(self.frame_content_wid_3)
        self.txtNClienteNut.setObjectName(u"txtNClienteNut")
        self.txtNClienteNut.setMinimumSize(QSize(200, 35))
        self.txtNClienteNut.setMaximumSize(QSize(900, 35))
        self.txtNClienteNut.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"color: rgb(0, 0, 0);")
        self.txtNClienteNut.setMaxLength(4)

        self.gridLayout_13.addWidget(self.txtNClienteNut, 0, 0, 1, 3)

        self.btnBNut = QPushButton(self.frame_content_wid_3)
        self.btnBNut.setObjectName(u"btnBNut")
        self.btnBNut.setMinimumSize(QSize(200, 35))
        self.btnBNut.setMaximumSize(QSize(200, 35))
        self.btnBNut.setFont(font3)
        self.btnBNut.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBNut.setAutoFillBackground(False)
        self.btnBNut.setStyleSheet(u"")

        self.gridLayout_13.addWidget(self.btnBNut, 0, 3, 1, 1)

        self.lblNClienteNut = QLabel(self.frame_content_wid_3)
        self.lblNClienteNut.setObjectName(u"lblNClienteNut")
        self.lblNClienteNut.setMinimumSize(QSize(425, 30))
        self.lblNClienteNut.setMaximumSize(QSize(900, 30))

        self.gridLayout_13.addWidget(self.lblNClienteNut, 1, 0, 1, 2)


        self.horizontalLayout_55.addLayout(self.gridLayout_13)

        self.label_36 = QLabel(self.frame_content_wid_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(100, 80))
        self.label_36.setStyleSheet(u"image: url(:/logo/LogoRESILIENCE2.png);")

        self.horizontalLayout_55.addWidget(self.label_36)


        self.verticalLayout_48.addWidget(self.frame_content_wid_3)


        self.verticalLayout_47.addWidget(self.frame_div_content_3)


        self.verticalLayout_43.addWidget(self.row_3)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(10)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, -1)
        self.tableWidget_3 = QTableWidget(self.lytNutriologo)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        font9 = QFont()
        font9.setBold(True)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem47.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        if (self.tableWidget_3.rowCount() < 19):
            self.tableWidget_3.setRowCount(19)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem49.setFont(font9);
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setVerticalHeaderItem(13, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(14, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(15, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(16, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(17, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(18, __qtablewidgetitem67)
        font10 = QFont()
        font10.setFamily(u"Montserrat")
        font10.setPointSize(11)
        font10.setBold(False)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setFont(font10);
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem69)
        font11 = QFont()
        font11.setPointSize(11)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setFont(font11);
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setFont(font11);
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setFont(font11);
        self.tableWidget_3.setItem(3, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setFont(font11);
        self.tableWidget_3.setItem(4, 0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setFont(font11);
        self.tableWidget_3.setItem(5, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setFont(font11);
        self.tableWidget_3.setItem(6, 0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setFont(font11);
        self.tableWidget_3.setItem(7, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setFont(font11);
        self.tableWidget_3.setItem(8, 0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setFont(font11);
        self.tableWidget_3.setItem(9, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setFont(font11);
        self.tableWidget_3.setItem(10, 0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setFont(font11);
        self.tableWidget_3.setItem(11, 0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setFont(font11);
        self.tableWidget_3.setItem(12, 0, __qtablewidgetitem82)
        font12 = QFont()
        font12.setPointSize(11)
        font12.setBold(False)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setFont(font12);
        self.tableWidget_3.setItem(13, 0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setFont(font11);
        self.tableWidget_3.setItem(14, 0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setFont(font11);
        self.tableWidget_3.setItem(15, 0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setFont(font11);
        self.tableWidget_3.setItem(16, 0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setFont(font11);
        self.tableWidget_3.setItem(17, 0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setFont(font11);
        self.tableWidget_3.setItem(18, 0, __qtablewidgetitem88)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy5.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy5)
        self.tableWidget_3.setMinimumSize(QSize(350, 0))
        self.tableWidget_3.setMaximumSize(QSize(470, 16777215))
        self.tableWidget_3.setStyleSheet(u"background-color: transparent;\n"
"gridline-color: transparent;\n"
"border-color: transparent;\n"
"font: 10pt \"Montserrat\";")
        self.tableWidget_3.setLineWidth(1)
        self.tableWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_3.setAutoScroll(True)
        self.tableWidget_3.setAutoScrollMargin(16)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.tableWidget_3.setTabKeyNavigation(True)
        self.tableWidget_3.setProperty("showDropIndicator", True)
        self.tableWidget_3.setDragEnabled(False)
        self.tableWidget_3.setDragDropOverwriteMode(True)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_3.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(165)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(55)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(55)

        self.horizontalLayout_51.addWidget(self.tableWidget_3)

        self.tableWidget_4 = QTableWidget(self.lytNutriologo)
        if (self.tableWidget_4.columnCount() < 2):
            self.tableWidget_4.setColumnCount(2)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem90)
        if (self.tableWidget_4.rowCount() < 12):
            self.tableWidget_4.setRowCount(12)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_4.setVerticalHeaderItem(0, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(4, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(5, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(6, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(7, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(8, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(9, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(10, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(11, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setFont(font11);
        self.tableWidget_4.setItem(0, 0, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setFont(font11);
        self.tableWidget_4.setItem(1, 0, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setFont(font11);
        self.tableWidget_4.setItem(2, 0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setFont(font11);
        self.tableWidget_4.setItem(3, 0, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setFont(font11);
        self.tableWidget_4.setItem(4, 0, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setFont(font11);
        self.tableWidget_4.setItem(5, 0, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setFont(font11);
        self.tableWidget_4.setItem(6, 0, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setFont(font11);
        self.tableWidget_4.setItem(7, 0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setFont(font11);
        self.tableWidget_4.setItem(8, 0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setFont(font11);
        self.tableWidget_4.setItem(9, 0, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        __qtablewidgetitem113.setFont(font11);
        self.tableWidget_4.setItem(10, 0, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        __qtablewidgetitem114.setFont(font11);
        self.tableWidget_4.setItem(11, 0, __qtablewidgetitem114)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        sizePolicy5.setHeightForWidth(self.tableWidget_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_4.setSizePolicy(sizePolicy5)
        self.tableWidget_4.setMinimumSize(QSize(350, 0))
        self.tableWidget_4.setMaximumSize(QSize(470, 16777215))
        self.tableWidget_4.setStyleSheet(u"background-color: transparent;\n"
"gridline-color: transparent;\n"
"border-color: transparent;\n"
"font: 10pt \"Montserrat\";")
        self.tableWidget_4.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.tableWidget_4.setAlternatingRowColors(True)
        self.tableWidget_4.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_4.horizontalHeader().setVisible(False)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(165)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget_4.horizontalHeader().setHighlightSections(True)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(55)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(55)

        self.horizontalLayout_51.addWidget(self.tableWidget_4)

        self.tableWidget_5 = QTableWidget(self.lytNutriologo)
        if (self.tableWidget_5.columnCount() < 2):
            self.tableWidget_5.setColumnCount(2)
        __qtablewidgetitem115 = QTableWidgetItem()
        __qtablewidgetitem115.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem116)
        if (self.tableWidget_5.rowCount() < 13):
            self.tableWidget_5.setRowCount(13)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(3, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(4, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(5, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(6, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(7, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(8, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(9, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(10, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(11, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(12, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setFont(font11);
        self.tableWidget_5.setItem(0, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setFont(font11);
        self.tableWidget_5.setItem(1, 0, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setFont(font11);
        self.tableWidget_5.setItem(2, 0, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        __qtablewidgetitem133.setFont(font11);
        self.tableWidget_5.setItem(3, 0, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        __qtablewidgetitem134.setFont(font11);
        self.tableWidget_5.setItem(4, 0, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        __qtablewidgetitem135.setFont(font11);
        self.tableWidget_5.setItem(5, 0, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setFont(font11);
        self.tableWidget_5.setItem(6, 0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        __qtablewidgetitem137.setFont(font11);
        self.tableWidget_5.setItem(7, 0, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        __qtablewidgetitem138.setFont(font11);
        self.tableWidget_5.setItem(8, 0, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        __qtablewidgetitem139.setFont(font11);
        self.tableWidget_5.setItem(9, 0, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        __qtablewidgetitem140.setFont(font11);
        self.tableWidget_5.setItem(10, 0, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        __qtablewidgetitem141.setFont(font11);
        self.tableWidget_5.setItem(11, 0, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        __qtablewidgetitem142.setFont(font11);
        self.tableWidget_5.setItem(12, 0, __qtablewidgetitem142)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        sizePolicy5.setHeightForWidth(self.tableWidget_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_5.setSizePolicy(sizePolicy5)
        self.tableWidget_5.setMinimumSize(QSize(350, 0))
        self.tableWidget_5.setMaximumSize(QSize(470, 16777215))
        self.tableWidget_5.setStyleSheet(u"background-color: transparent;\n"
"gridline-color: transparent;\n"
"border-color: transparent;\n"
"font: 10pt \"Montserrat\";")
        self.tableWidget_5.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.tableWidget_5.setAlternatingRowColors(True)
        self.tableWidget_5.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_5.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_5.horizontalHeader().setVisible(False)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(165)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget_5.horizontalHeader().setHighlightSections(True)
        self.tableWidget_5.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.tableWidget_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_5.verticalHeader().setMinimumSectionSize(55)
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(55)
        self.tableWidget_5.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_51.addWidget(self.tableWidget_5)


        self.verticalLayout_43.addLayout(self.horizontalLayout_51)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(50)
        self.gridLayout_12.setVerticalSpacing(10)
        self.btnImgNut4 = QPushButton(self.lytNutriologo)
        self.btnImgNut4.setObjectName(u"btnImgNut4")
        self.btnImgNut4.setEnabled(False)
        self.btnImgNut4.setMinimumSize(QSize(100, 40))
        self.btnImgNut4.setMaximumSize(QSize(150, 40))
        self.btnImgNut4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnImgNut4.setStyleSheet(u"background-color: rgb(223, 40, 41);\n"
"color: rgb(221, 221, 221);\n"
"")

        self.gridLayout_12.addWidget(self.btnImgNut4, 2, 2, 1, 1)

        self.lblPersonalizado = QLabel(self.lytNutriologo)
        self.lblPersonalizado.setObjectName(u"lblPersonalizado")
        self.lblPersonalizado.setMinimumSize(QSize(0, 25))
        self.lblPersonalizado.setMaximumSize(QSize(1600, 25))
        self.lblPersonalizado.setStyleSheet(u"font: 11pt \"Montserrat\";\n"
"background-color: rgb(221, 221, 221);")

        self.gridLayout_12.addWidget(self.lblPersonalizado, 1, 3, 1, 3)

        self.btnImgNut1 = QPushButton(self.lytNutriologo)
        self.btnImgNut1.setObjectName(u"btnImgNut1")
        self.btnImgNut1.setEnabled(False)
        self.btnImgNut1.setMinimumSize(QSize(100, 40))
        self.btnImgNut1.setMaximumSize(QSize(150, 40))
        self.btnImgNut1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnImgNut1.setAutoFillBackground(False)
        self.btnImgNut1.setStyleSheet(u"background-color: rgb(223, 40, 41);\n"
"color: rgb(221, 221, 221);\n"
"")
        self.btnImgNut1.setCheckable(False)
        self.btnImgNut1.setAutoDefault(False)
        self.btnImgNut1.setFlat(False)

        self.gridLayout_12.addWidget(self.btnImgNut1, 2, 1, 1, 1)

        self.cmbFechaImg = QComboBox(self.lytNutriologo)
        self.cmbFechaImg.setObjectName(u"cmbFechaImg")
        self.cmbFechaImg.setEnabled(False)
        self.cmbFechaImg.setMaximumSize(QSize(160, 16777215))
        self.cmbFechaImg.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbFechaImg.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: rgb(100, 100,100 );")
        self.cmbFechaImg.setMaxVisibleItems(100)

        self.gridLayout_12.addWidget(self.cmbFechaImg, 2, 0, 1, 1)

        self.cmbSubirDieta = QComboBox(self.lytNutriologo)
        self.cmbSubirDieta.setObjectName(u"cmbSubirDieta")
        self.cmbSubirDieta.setEnabled(False)
        self.cmbSubirDieta.setMinimumSize(QSize(170, 0))
        self.cmbSubirDieta.setMaximumSize(QSize(170, 16777215))
        self.cmbSubirDieta.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbSubirDieta.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: rgb(100, 100,100 );")
        self.cmbSubirDieta.setMaxVisibleItems(100)

        self.gridLayout_12.addWidget(self.cmbSubirDieta, 2, 3, 1, 1)

        self.lblFotografias = QLabel(self.lytNutriologo)
        self.lblFotografias.setObjectName(u"lblFotografias")
        self.lblFotografias.setMinimumSize(QSize(0, 25))
        self.lblFotografias.setMaximumSize(QSize(1600, 25))
        self.lblFotografias.setStyleSheet(u"font: 11pt \"Montserrat\";\n"
"background-color: rgb(221, 221, 221);")

        self.gridLayout_12.addWidget(self.lblFotografias, 1, 0, 1, 3)

        self.btnSubirDieta = QPushButton(self.lytNutriologo)
        self.btnSubirDieta.setObjectName(u"btnSubirDieta")
        self.btnSubirDieta.setEnabled(False)
        self.btnSubirDieta.setMinimumSize(QSize(100, 40))
        self.btnSubirDieta.setMaximumSize(QSize(150, 40))
        self.btnSubirDieta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSubirDieta.setStyleSheet(u"background-color: rgb(223, 40, 41);\n"
"color: rgb(221, 221, 221);\n"
"")
        self.btnSubirDieta.setAutoDefault(False)
        self.btnSubirDieta.setFlat(False)

        self.gridLayout_12.addWidget(self.btnSubirDieta, 2, 5, 1, 1)

        self.lblAbrirImg = QPushButton(self.lytNutriologo)
        self.lblAbrirImg.setObjectName(u"lblAbrirImg")
        self.lblAbrirImg.setEnabled(False)
        self.lblAbrirImg.setMinimumSize(QSize(40, 40))
        self.lblAbrirImg.setMaximumSize(QSize(40, 40))
        self.lblAbrirImg.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblAbrirImg.setStyleSheet(u"background-color: rgb(223, 40, 41);\n"
"image: url(:/icons/images/icons/cil-folder-open.png);\n"
"color: rgb(221, 221, 221);\n"
"")

        self.gridLayout_12.addWidget(self.lblAbrirImg, 2, 4, 1, 1)

        self.lblFileName = QLabel(self.lytNutriologo)
        self.lblFileName.setObjectName(u"lblFileName")

        self.gridLayout_12.addWidget(self.lblFileName, 3, 3, 1, 3)

        self.label_17 = QLabel(self.lytNutriologo)
        self.label_17.setObjectName(u"label_17")
        sizePolicy7.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy7)
        self.label_17.setMinimumSize(QSize(170, 0))
        self.label_17.setMaximumSize(QSize(170, 16777215))
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_17, 0, 3, 1, 1)


        self.verticalLayout_43.addLayout(self.gridLayout_12)

        self.stackedWidget.addWidget(self.lytNutriologo)
        self.lytImgDieta = QWidget()
        self.lytImgDieta.setObjectName(u"lytImgDieta")
        self.verticalLayout_10 = QVBoxLayout(self.lytImgDieta)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lblImgDieta = QLabel(self.lytImgDieta)
        self.lblImgDieta.setObjectName(u"lblImgDieta")
        self.lblImgDieta.setMaximumSize(QSize(1100, 600))
        self.lblImgDieta.setStyleSheet(u"border: 2px solid rgb(33, 37, 43);\n"
"border-radius: 5px;\n"
"")
        self.lblImgDieta.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.lblImgDieta)

        self.stackedWidget.addWidget(self.lytImgDieta)
        self.lytPsicologo = QWidget()
        self.lytPsicologo.setObjectName(u"lytPsicologo")
        self.verticalLayout_44 = QVBoxLayout(self.lytPsicologo)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.txtNClientePsi = QLineEdit(self.lytPsicologo)
        self.txtNClientePsi.setObjectName(u"txtNClientePsi")
        sizePolicy4.setHeightForWidth(self.txtNClientePsi.sizePolicy().hasHeightForWidth())
        self.txtNClientePsi.setSizePolicy(sizePolicy4)
        self.txtNClientePsi.setMinimumSize(QSize(0, 35))
        self.txtNClientePsi.setMaximumSize(QSize(425, 35))
        self.txtNClientePsi.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(100, 100,100 );\n"
"font: 10pt \"Montserrat\";\n"
"selection-background-color: rgb(237, 28, 40);\n"
"")
        self.txtNClientePsi.setMaxLength(5)

        self.gridLayout_9.addWidget(self.txtNClientePsi, 0, 0, 1, 1)

        self.btnBPsi = QPushButton(self.lytPsicologo)
        self.btnBPsi.setObjectName(u"btnBPsi")
        self.btnBPsi.setMinimumSize(QSize(200, 35))
        self.btnBPsi.setMaximumSize(QSize(200, 35))
        self.btnBPsi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBPsi.setStyleSheet(u"background-color: rgb(237, 28, 40);\n"
"font: 11pt \"Montserrat\";")

        self.gridLayout_9.addWidget(self.btnBPsi, 0, 1, 1, 1)

        self.lblNClientePsi = QLabel(self.lytPsicologo)
        self.lblNClientePsi.setObjectName(u"lblNClientePsi")
        self.lblNClientePsi.setMinimumSize(QSize(0, 30))
        self.lblNClientePsi.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_9.addWidget(self.lblNClientePsi, 1, 0, 1, 1)

        self.btnCSPsi = QPushButton(self.lytPsicologo)
        self.btnCSPsi.setObjectName(u"btnCSPsi")
        self.btnCSPsi.setMinimumSize(QSize(0, 35))
        self.btnCSPsi.setMaximumSize(QSize(200, 35))
        font13 = QFont()
        font13.setFamily(u"Montserrat")
        font13.setPointSize(11)
        font13.setBold(False)
        font13.setItalic(False)
        self.btnCSPsi.setFont(font13)
        self.btnCSPsi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCSPsi.setAutoFillBackground(False)
        self.btnCSPsi.setStyleSheet(u"background-color: rgb(237, 28, 40\n"
");\n"
"font: 11pt \"Montserrat\";")

        self.gridLayout_9.addWidget(self.btnCSPsi, 2, 0, 1, 1)


        self.verticalLayout_44.addLayout(self.gridLayout_9)

        self.stackedWidget.addWidget(self.lytPsicologo)
        self.lytEntrenador = QWidget()
        self.lytEntrenador.setObjectName(u"lytEntrenador")
        self.verticalLayout_45 = QVBoxLayout(self.lytEntrenador)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lblNClienteEnt = QLabel(self.lytEntrenador)
        self.lblNClienteEnt.setObjectName(u"lblNClienteEnt")
        self.lblNClienteEnt.setMinimumSize(QSize(0, 30))
        self.lblNClienteEnt.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.lblNClienteEnt, 1, 0, 1, 1)

        self.txtNClienteEnt = QLineEdit(self.lytEntrenador)
        self.txtNClienteEnt.setObjectName(u"txtNClienteEnt")
        sizePolicy4.setHeightForWidth(self.txtNClienteEnt.sizePolicy().hasHeightForWidth())
        self.txtNClienteEnt.setSizePolicy(sizePolicy4)
        self.txtNClienteEnt.setMinimumSize(QSize(0, 35))
        self.txtNClienteEnt.setMaximumSize(QSize(425, 35))
        self.txtNClienteEnt.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(100, 100,100 );\n"
"font: 10pt \"Montserrat\";\n"
"selection-background-color: rgb(237, 28, 40);\n"
"")
        self.txtNClienteEnt.setMaxLength(5)

        self.gridLayout_10.addWidget(self.txtNClienteEnt, 0, 0, 1, 1)

        self.btnBEnt = QPushButton(self.lytEntrenador)
        self.btnBEnt.setObjectName(u"btnBEnt")
        self.btnBEnt.setMinimumSize(QSize(200, 35))
        self.btnBEnt.setMaximumSize(QSize(200, 35))
        self.btnBEnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBEnt.setStyleSheet(u"background-color: rgb(237, 28, 40);\n"
"font: 11pt \"Montserrat\";")

        self.gridLayout_10.addWidget(self.btnBEnt, 0, 1, 1, 1)

        self.btnCSEnt = QPushButton(self.lytEntrenador)
        self.btnCSEnt.setObjectName(u"btnCSEnt")
        self.btnCSEnt.setMinimumSize(QSize(0, 35))
        self.btnCSEnt.setMaximumSize(QSize(200, 35))
        self.btnCSEnt.setFont(font13)
        self.btnCSEnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCSEnt.setAutoFillBackground(False)
        self.btnCSEnt.setStyleSheet(u"background-color: rgb(237, 28, 40\n"
");\n"
"font: 11pt \"Montserrat\";")

        self.gridLayout_10.addWidget(self.btnCSEnt, 2, 0, 1, 1)


        self.verticalLayout_45.addLayout(self.gridLayout_10)

        self.stackedWidget.addWidget(self.lytEntrenador)
        self.lytNotificacion = QWidget()
        self.lytNotificacion.setObjectName(u"lytNotificacion")
        self.lytNotificacion.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(237, 28, 40);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	image: url(:/images/flecha-hacia-abajo.png);\n"
""
                        "	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(237, 28, 40);\n"
"	font: 12pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(238, 56, 67);\n"
"	border: 2px solid rgb(238, 56, 67);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(237, 28, 40);\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.lytNotificacion)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_52.setContentsMargins(-1, 30, -1, 50)
        self.lblLogoReservar_5 = QLabel(self.lytNotificacion)
        self.lblLogoReservar_5.setObjectName(u"lblLogoReservar_5")
        self.lblLogoReservar_5.setMinimumSize(QSize(500, 100))
        self.lblLogoReservar_5.setMaximumSize(QSize(500, 100))
        self.lblLogoReservar_5.setStyleSheet(u"image: url(:/images/images/images/LogoRESILIENCE2.png);")

        self.horizontalLayout_52.addWidget(self.lblLogoReservar_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_52)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setVerticalSpacing(20)
        self.gridLayout_11.setContentsMargins(-1, 100, -1, -1)
        self.ntTxtTexto = QLineEdit(self.lytNotificacion)
        self.ntTxtTexto.setObjectName(u"ntTxtTexto")
        self.ntTxtTexto.setMinimumSize(QSize(0, 45))
        self.ntTxtTexto.setMaximumSize(QSize(450, 45))
        self.ntTxtTexto.setStyleSheet(u"")
        self.ntTxtTexto.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.ntTxtTexto.setMaxLength(255)
        self.ntTxtTexto.setClearButtonEnabled(True)

        self.gridLayout_11.addWidget(self.ntTxtTexto, 3, 0, 1, 1)

        self.ntCmbRemitente = QComboBox(self.lytNotificacion)
        self.ntCmbRemitente.setObjectName(u"ntCmbRemitente")
        self.ntCmbRemitente.setMinimumSize(QSize(450, 45))
        self.ntCmbRemitente.setMaximumSize(QSize(450, 45))
        self.ntCmbRemitente.setCursor(QCursor(Qt.PointingHandCursor))
        self.ntCmbRemitente.setMaxVisibleItems(5)
        self.ntCmbRemitente.setInsertPolicy(QComboBox.InsertAtBottom)
        self.ntCmbRemitente.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.ntCmbRemitente.setModelColumn(0)

        self.gridLayout_11.addWidget(self.ntCmbRemitente, 5, 0, 1, 1)

        self.ntTxtNumCliente = QLineEdit(self.lytNotificacion)
        self.ntTxtNumCliente.setObjectName(u"ntTxtNumCliente")
        self.ntTxtNumCliente.setEnabled(False)
        self.ntTxtNumCliente.setMinimumSize(QSize(0, 45))
        self.ntTxtNumCliente.setMaximumSize(QSize(450, 45))
        self.ntTxtNumCliente.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: rgb(100, 100,100 );")
        self.ntTxtNumCliente.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.ntTxtNumCliente.setMaxLength(4)
        self.ntTxtNumCliente.setClearButtonEnabled(True)

        self.gridLayout_11.addWidget(self.ntTxtNumCliente, 5, 1, 1, 1)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.ntBtnEnviar = QPushButton(self.lytNotificacion)
        self.ntBtnEnviar.setObjectName(u"ntBtnEnviar")
        self.ntBtnEnviar.setMinimumSize(QSize(0, 35))
        self.ntBtnEnviar.setMaximumSize(QSize(200, 35))
        self.ntBtnEnviar.setCursor(QCursor(Qt.PointingHandCursor))
        self.ntBtnEnviar.setStyleSheet(u"")

        self.horizontalLayout_53.addWidget(self.ntBtnEnviar)


        self.gridLayout_11.addLayout(self.horizontalLayout_53, 7, 0, 1, 1)

        self.ntTxtTitulo = QLineEdit(self.lytNotificacion)
        self.ntTxtTitulo.setObjectName(u"ntTxtTitulo")
        self.ntTxtTitulo.setMinimumSize(QSize(0, 45))
        self.ntTxtTitulo.setMaximumSize(QSize(450, 45))
        self.ntTxtTitulo.setStyleSheet(u"")
        self.ntTxtTitulo.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.ntTxtTitulo.setMaxLength(255)
        self.ntTxtTitulo.setClearButtonEnabled(True)

        self.gridLayout_11.addWidget(self.ntTxtTitulo, 1, 0, 1, 1)

        self.ntLblCmbRemitente = QLabel(self.lytNotificacion)
        self.ntLblCmbRemitente.setObjectName(u"ntLblCmbRemitente")
        self.ntLblCmbRemitente.setMinimumSize(QSize(0, 30))
        self.ntLblCmbRemitente.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.ntLblCmbRemitente, 6, 0, 1, 1)

        self.ntLblTexto = QLabel(self.lytNotificacion)
        self.ntLblTexto.setObjectName(u"ntLblTexto")
        self.ntLblTexto.setMinimumSize(QSize(0, 30))
        self.ntLblTexto.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.ntLblTexto, 4, 0, 1, 1)

        self.ntLblUrl = QLabel(self.lytNotificacion)
        self.ntLblUrl.setObjectName(u"ntLblUrl")
        self.ntLblUrl.setMinimumSize(QSize(0, 30))
        self.ntLblUrl.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.ntLblUrl, 6, 1, 1, 1)

        self.ntLblBtnEnviar = QLabel(self.lytNotificacion)
        self.ntLblBtnEnviar.setObjectName(u"ntLblBtnEnviar")

        self.gridLayout_11.addWidget(self.ntLblBtnEnviar, 8, 0, 1, 1)

        self.ntLblTitulo = QLabel(self.lytNotificacion)
        self.ntLblTitulo.setObjectName(u"ntLblTitulo")
        self.ntLblTitulo.setMinimumSize(QSize(0, 30))
        self.ntLblTitulo.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.ntLblTitulo, 2, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_11)

        self.stackedWidget.addWidget(self.lytNotificacion)
        self.lytLogin = QWidget()
        self.lytLogin.setObjectName(u"lytLogin")
        self.lytLogin.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(237, 28, 40);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	image: url(:/images/flecha-hacia-abajo.png);\n"
""
                        "	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(237, 28, 40);\n"
"	font: 12pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(238, 56, 67);\n"
"	border: 2px solid rgb(238, 56, 67);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(237, 28, 40);\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.lytLogin)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lblLogoLogin = QLabel(self.lytLogin)
        self.lblLogoLogin.setObjectName(u"lblLogoLogin")
        self.lblLogoLogin.setMinimumSize(QSize(400, 140))
        self.lblLogoLogin.setMaximumSize(QSize(400, 140))
        self.lblLogoLogin.setAutoFillBackground(False)
        self.lblLogoLogin.setStyleSheet(u"image: url(:/images/IMAGOTIPO.png);")
        self.lblLogoLogin.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.lblLogoLogin)


        self.verticalLayout_29.addLayout(self.horizontalLayout_15)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_35 = QLabel(self.lytLogin)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(250, 30))

        self.gridLayout_3.addWidget(self.label_35, 0, 2, 1, 1)

        self.label_22 = QLabel(self.lytLogin)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(250, 30))

        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)

        self.txtUsuario = QLineEdit(self.lytLogin)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setEnabled(True)
        self.txtUsuario.setMinimumSize(QSize(0, 45))
        self.txtUsuario.setMaximumSize(QSize(450, 45))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        brush23 = QBrush(QColor(221, 221, 221, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush23)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush23)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush23)
        brush24 = QBrush(QColor(237, 28, 40, 255))
        brush24.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush24)
        brush25 = QBrush(QColor(255, 255, 255, 255))
        brush25.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush23)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush23)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush23)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush24)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush23)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush23)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush23)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush24)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.txtUsuario.setPalette(palette2)
        self.txtUsuario.setAcceptDrops(True)
        self.txtUsuario.setStyleSheet(u"")
        self.txtUsuario.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.txtUsuario.setMaxLength(100)
        self.txtUsuario.setFrame(True)
        self.txtUsuario.setDragEnabled(False)
        self.txtUsuario.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txtUsuario.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.txtUsuario, 0, 1, 1, 1)

        self.label_6 = QLabel(self.lytLogin)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(500, 30))

        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)


        self.verticalLayout_29.addLayout(self.gridLayout_3)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.txtContrasea = QLineEdit(self.lytLogin)
        self.txtContrasea.setObjectName(u"txtContrasea")
        self.txtContrasea.setMinimumSize(QSize(0, 45))
        self.txtContrasea.setMaximumSize(QSize(450, 45))
        self.txtContrasea.setStyleSheet(u"")
        self.txtContrasea.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.txtContrasea.setMaxLength(100)
        self.txtContrasea.setEchoMode(QLineEdit.Password)
        self.txtContrasea.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.txtContrasea, 0, 1, 1, 1)

        self.label_43 = QLabel(self.lytLogin)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(250, 30))

        self.gridLayout_5.addWidget(self.label_43, 0, 0, 1, 1)

        self.label_42 = QLabel(self.lytLogin)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(250, 30))

        self.gridLayout_5.addWidget(self.label_42, 0, 2, 1, 1)

        self.label_14 = QLabel(self.lytLogin)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(500, 30))

        self.gridLayout_5.addWidget(self.label_14, 1, 1, 1, 1)


        self.verticalLayout_29.addLayout(self.gridLayout_5)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_40 = QLabel(self.lytLogin)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(250, 30))

        self.gridLayout_7.addWidget(self.label_40, 0, 0, 1, 1)

        self.label_41 = QLabel(self.lytLogin)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(250, 30))

        self.gridLayout_7.addWidget(self.label_41, 0, 2, 1, 1)

        self.label_18 = QLabel(self.lytLogin)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(500, 30))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_18, 1, 1, 1, 1)

        self.cmbTipoDeUsuario = QComboBox(self.lytLogin)
        self.cmbTipoDeUsuario.addItem("")
        self.cmbTipoDeUsuario.addItem("")
        self.cmbTipoDeUsuario.addItem("")
        self.cmbTipoDeUsuario.setObjectName(u"cmbTipoDeUsuario")
        self.cmbTipoDeUsuario.setMinimumSize(QSize(0, 45))
        self.cmbTipoDeUsuario.setMaximumSize(QSize(450, 45))
        self.cmbTipoDeUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbTipoDeUsuario.setStyleSheet(u"")
        self.cmbTipoDeUsuario.setMaxVisibleItems(3)
        self.cmbTipoDeUsuario.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.cmbTipoDeUsuario.setFrame(True)

        self.gridLayout_7.addWidget(self.cmbTipoDeUsuario, 0, 1, 1, 1)


        self.verticalLayout_29.addLayout(self.gridLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnIniciarSesion = QPushButton(self.lytLogin)
        self.btnIniciarSesion.setObjectName(u"btnIniciarSesion")
        self.btnIniciarSesion.setMaximumSize(QSize(300, 40))
        self.btnIniciarSesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnIniciarSesion.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.btnIniciarSesion)


        self.verticalLayout_29.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.lytLogin)
        self.lytRegistroUsuario = QWidget()
        self.lytRegistroUsuario.setObjectName(u"lytRegistroUsuario")
        self.lytRegistroUsuario.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(237, 28, 40);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(221, 221, 221);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	image: url(:/images/flecha-hacia-abajo.png);\n"
""
                        "	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(221, 221, 221);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(237, 28, 40);\n"
"	font: 12pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(238, 56, 67);\n"
"	border: 2px solid rgb(238, 56, 67);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(237, 28, 40);\n"
"	border: 2px solid rgb(237, 28, 40);\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.lytRegistroUsuario)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 20, -1, 20)
        self.lblLogoRegistro = QLabel(self.lytRegistroUsuario)
        self.lblLogoRegistro.setObjectName(u"lblLogoRegistro")
        self.lblLogoRegistro.setMinimumSize(QSize(400, 140))
        self.lblLogoRegistro.setMaximumSize(QSize(400, 140))
        self.lblLogoRegistro.setStyleSheet(u"image: url(:/images/IMAGOTIPO.png);")
        self.lblLogoRegistro.setScaledContents(False)

        self.horizontalLayout_14.addWidget(self.lblLogoRegistro)


        self.verticalLayout_20.addLayout(self.horizontalLayout_14)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_23 = QLabel(self.lytRegistroUsuario)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(70, 30))
        self.label_23.setMaximumSize(QSize(70, 30))
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_23)

        self.txtNombre = QLineEdit(self.lytRegistroUsuario)
        self.txtNombre.setObjectName(u"txtNombre")
        sizePolicy4.setHeightForWidth(self.txtNombre.sizePolicy().hasHeightForWidth())
        self.txtNombre.setSizePolicy(sizePolicy4)
        self.txtNombre.setMinimumSize(QSize(450, 45))
        self.txtNombre.setMaximumSize(QSize(450, 45))
        self.txtNombre.setStyleSheet(u"")
        self.txtNombre.setMaxLength(100)
        self.txtNombre.setEchoMode(QLineEdit.Normal)
        self.txtNombre.setDragEnabled(False)
        self.txtNombre.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txtNombre.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.txtNombre)

        self.label_19 = QLabel(self.lytRegistroUsuario)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(70, 30))
        self.label_19.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_17.addWidget(self.label_19)


        self.verticalLayout_25.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lblNombre = QLabel(self.lytRegistroUsuario)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_18.addWidget(self.lblNombre)


        self.verticalLayout_25.addLayout(self.horizontalLayout_18)


        self.verticalLayout_22.addLayout(self.verticalLayout_25)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_44 = QLabel(self.lytRegistroUsuario)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(70, 30))
        self.label_44.setMaximumSize(QSize(70, 30))
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_44)

        self.txtApellido = QLineEdit(self.lytRegistroUsuario)
        self.txtApellido.setObjectName(u"txtApellido")
        sizePolicy4.setHeightForWidth(self.txtApellido.sizePolicy().hasHeightForWidth())
        self.txtApellido.setSizePolicy(sizePolicy4)
        self.txtApellido.setMinimumSize(QSize(450, 45))
        self.txtApellido.setMaximumSize(QSize(450, 45))
        self.txtApellido.setStyleSheet(u"")
        self.txtApellido.setMaxLength(100)
        self.txtApellido.setDragEnabled(False)
        self.txtApellido.setClearButtonEnabled(True)

        self.horizontalLayout_22.addWidget(self.txtApellido)

        self.label_45 = QLabel(self.lytRegistroUsuario)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(70, 30))
        self.label_45.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_22.addWidget(self.label_45)


        self.verticalLayout_28.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lblApellido = QLabel(self.lytRegistroUsuario)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_23.addWidget(self.lblApellido)


        self.verticalLayout_28.addLayout(self.horizontalLayout_23)


        self.verticalLayout_22.addLayout(self.verticalLayout_28)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.lytRegistroUsuario)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 30))
        self.label_4.setMaximumSize(QSize(70, 30))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.txtCorreo = QLineEdit(self.lytRegistroUsuario)
        self.txtCorreo.setObjectName(u"txtCorreo")
        sizePolicy4.setHeightForWidth(self.txtCorreo.sizePolicy().hasHeightForWidth())
        self.txtCorreo.setSizePolicy(sizePolicy4)
        self.txtCorreo.setMinimumSize(QSize(450, 45))
        self.txtCorreo.setMaximumSize(QSize(450, 45))
        self.txtCorreo.setStyleSheet(u"")
        self.txtCorreo.setMaxLength(100)
        self.txtCorreo.setClearButtonEnabled(True)

        self.horizontalLayout_7.addWidget(self.txtCorreo)

        self.label_20 = QLabel(self.lytRegistroUsuario)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(70, 30))
        self.label_20.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_7.addWidget(self.label_20)


        self.verticalLayout_21.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lblCorreo = QLabel(self.lytRegistroUsuario)
        self.lblCorreo.setObjectName(u"lblCorreo")
        self.lblCorreo.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_13.addWidget(self.lblCorreo)


        self.verticalLayout_21.addLayout(self.horizontalLayout_13)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_29 = QLabel(self.lytRegistroUsuario)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(70, 30))
        self.label_29.setMaximumSize(QSize(70, 30))
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_29)

        self.txtTelefono = QLineEdit(self.lytRegistroUsuario)
        self.txtTelefono.setObjectName(u"txtTelefono")
        sizePolicy4.setHeightForWidth(self.txtTelefono.sizePolicy().hasHeightForWidth())
        self.txtTelefono.setSizePolicy(sizePolicy4)
        self.txtTelefono.setMinimumSize(QSize(450, 45))
        self.txtTelefono.setMaximumSize(QSize(450, 45))
        self.txtTelefono.setAutoFillBackground(False)
        self.txtTelefono.setStyleSheet(u"")
        self.txtTelefono.setMaxLength(10)
        self.txtTelefono.setClearButtonEnabled(True)

        self.horizontalLayout_19.addWidget(self.txtTelefono)

        self.label_21 = QLabel(self.lytRegistroUsuario)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(70, 30))
        self.label_21.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_19.addWidget(self.label_21)


        self.verticalLayout_26.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lblTelefono = QLabel(self.lytRegistroUsuario)
        self.lblTelefono.setObjectName(u"lblTelefono")
        self.lblTelefono.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_20.addWidget(self.lblTelefono)


        self.verticalLayout_26.addLayout(self.horizontalLayout_20)


        self.verticalLayout_22.addLayout(self.verticalLayout_26)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_30 = QLabel(self.lytRegistroUsuario)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 30))
        self.label_30.setMaximumSize(QSize(16777215, 30))
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_30)

        self.txtEdad = QLineEdit(self.lytRegistroUsuario)
        self.txtEdad.setObjectName(u"txtEdad")
        sizePolicy4.setHeightForWidth(self.txtEdad.sizePolicy().hasHeightForWidth())
        self.txtEdad.setSizePolicy(sizePolicy4)
        self.txtEdad.setMinimumSize(QSize(144, 45))
        self.txtEdad.setMaximumSize(QSize(144, 45))
        self.txtEdad.setStyleSheet(u"")
        self.txtEdad.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)
        self.txtEdad.setMaxLength(2)
        self.txtEdad.setClearButtonEnabled(True)

        self.horizontalLayout_24.addWidget(self.txtEdad)

        self.txtAltura = QLineEdit(self.lytRegistroUsuario)
        self.txtAltura.setObjectName(u"txtAltura")
        sizePolicy4.setHeightForWidth(self.txtAltura.sizePolicy().hasHeightForWidth())
        self.txtAltura.setSizePolicy(sizePolicy4)
        self.txtAltura.setMinimumSize(QSize(143, 45))
        self.txtAltura.setMaximumSize(QSize(143, 45))
        self.txtAltura.setStyleSheet(u"")
        self.txtAltura.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)
        self.txtAltura.setMaxLength(4)
        self.txtAltura.setClearButtonEnabled(True)

        self.horizontalLayout_24.addWidget(self.txtAltura)

        self.txtPeso = QLineEdit(self.lytRegistroUsuario)
        self.txtPeso.setObjectName(u"txtPeso")
        sizePolicy4.setHeightForWidth(self.txtPeso.sizePolicy().hasHeightForWidth())
        self.txtPeso.setSizePolicy(sizePolicy4)
        self.txtPeso.setMinimumSize(QSize(143, 45))
        self.txtPeso.setMaximumSize(QSize(143, 45))
        self.txtPeso.setStyleSheet(u"")
        self.txtPeso.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)
        self.txtPeso.setMaxLength(6)
        self.txtPeso.setClearButtonEnabled(True)

        self.horizontalLayout_24.addWidget(self.txtPeso)

        self.label_24 = QLabel(self.lytRegistroUsuario)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 30))
        self.label_24.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_24.addWidget(self.label_24)


        self.verticalLayout_30.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_13 = QLabel(self.lytRegistroUsuario)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_25.addWidget(self.label_13)

        self.lblEdad = QLabel(self.lytRegistroUsuario)
        self.lblEdad.setObjectName(u"lblEdad")
        self.lblEdad.setMaximumSize(QSize(144, 30))

        self.horizontalLayout_25.addWidget(self.lblEdad)

        self.lblEstatura = QLabel(self.lytRegistroUsuario)
        self.lblEstatura.setObjectName(u"lblEstatura")
        self.lblEstatura.setMaximumSize(QSize(143, 30))

        self.horizontalLayout_25.addWidget(self.lblEstatura)

        self.lblPeso = QLabel(self.lytRegistroUsuario)
        self.lblPeso.setObjectName(u"lblPeso")
        self.lblPeso.setMaximumSize(QSize(143, 30))

        self.horizontalLayout_25.addWidget(self.lblPeso)

        self.label_15 = QLabel(self.lytRegistroUsuario)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_25.addWidget(self.label_15)


        self.verticalLayout_30.addLayout(self.horizontalLayout_25)


        self.verticalLayout_22.addLayout(self.verticalLayout_30)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_54 = QLabel(self.lytRegistroUsuario)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(70, 30))
        self.label_54.setMaximumSize(QSize(70, 30))
        self.label_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_54)

        self.cmbTipoSexo = QComboBox(self.lytRegistroUsuario)
        self.cmbTipoSexo.addItem("")
        self.cmbTipoSexo.addItem("")
        self.cmbTipoSexo.setObjectName(u"cmbTipoSexo")
        self.cmbTipoSexo.setMinimumSize(QSize(450, 45))
        self.cmbTipoSexo.setMaximumSize(QSize(450, 45))
        self.cmbTipoSexo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbTipoSexo.setStyleSheet(u"")
        self.cmbTipoSexo.setMaxVisibleItems(2)

        self.horizontalLayout_26.addWidget(self.cmbTipoSexo)

        self.label_55 = QLabel(self.lytRegistroUsuario)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(70, 30))
        self.label_55.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_26.addWidget(self.label_55)


        self.verticalLayout_31.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lblTipoMembresia = QLabel(self.lytRegistroUsuario)
        self.lblTipoMembresia.setObjectName(u"lblTipoMembresia")
        self.lblTipoMembresia.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_27.addWidget(self.lblTipoMembresia)


        self.verticalLayout_31.addLayout(self.horizontalLayout_27)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_58 = QLabel(self.lytRegistroUsuario)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(70, 30))
        self.label_58.setMaximumSize(QSize(70, 30))
        self.label_58.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_58)

        self.cmbNivel = QComboBox(self.lytRegistroUsuario)
        self.cmbNivel.setObjectName(u"cmbNivel")
        self.cmbNivel.setMinimumSize(QSize(450, 45))
        self.cmbNivel.setMaximumSize(QSize(450, 45))
        self.cmbNivel.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbNivel.setStyleSheet(u"")
        self.cmbNivel.setMaxVisibleItems(3)

        self.horizontalLayout_31.addWidget(self.cmbNivel)

        self.label_59 = QLabel(self.lytRegistroUsuario)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(70, 30))
        self.label_59.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_31.addWidget(self.label_59)


        self.verticalLayout_46.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lblTipoMembresia_3 = QLabel(self.lytRegistroUsuario)
        self.lblTipoMembresia_3.setObjectName(u"lblTipoMembresia_3")
        self.lblTipoMembresia_3.setMaximumSize(QSize(450, 30))

        self.horizontalLayout_32.addWidget(self.lblTipoMembresia_3)


        self.verticalLayout_46.addLayout(self.horizontalLayout_32)


        self.verticalLayout_31.addLayout(self.verticalLayout_46)


        self.verticalLayout_22.addLayout(self.verticalLayout_31)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btnRegistrar = QPushButton(self.lytRegistroUsuario)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setMinimumSize(QSize(0, 35))
        self.btnRegistrar.setMaximumSize(QSize(200, 35))
        self.btnRegistrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegistrar.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.btnRegistrar)


        self.verticalLayout_22.addLayout(self.horizontalLayout_16)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lblRegistrar = QLabel(self.lytRegistroUsuario)
        self.lblRegistrar.setObjectName(u"lblRegistrar")
        self.lblRegistrar.setMaximumSize(QSize(400, 30))
        self.lblRegistrar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lblRegistrar)


        self.verticalLayout_27.addLayout(self.horizontalLayout_21)


        self.verticalLayout_22.addLayout(self.verticalLayout_27)


        self.verticalLayout_20.addLayout(self.verticalLayout_22)

        self.stackedWidget.addWidget(self.lytRegistroUsuario)
        self.lytWeb = QWidget()
        self.lytWeb.setObjectName(u"lytWeb")
        self.verticalLayout_7 = QVBoxLayout(self.lytWeb)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setSpacing(5)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.lblfoto1 = QLabel(self.lytWeb)
        self.lblfoto1.setObjectName(u"lblfoto1")
        self.lblfoto1.setMaximumSize(QSize(400, 700))
        self.lblfoto1.setStyleSheet(u"border: 2px solid rgb(33, 37, 43);\n"
"border-radius: 5px;\n"
"")
        self.lblfoto1.setScaledContents(True)

        self.horizontalLayout_56.addWidget(self.lblfoto1)

        self.lblfoto2 = QLabel(self.lytWeb)
        self.lblfoto2.setObjectName(u"lblfoto2")
        self.lblfoto2.setMaximumSize(QSize(400, 700))
        self.lblfoto2.setStyleSheet(u"border: 2px solid rgb(33, 37, 43);\n"
"border-radius: 5px;\n"
"")
        self.lblfoto2.setScaledContents(True)

        self.horizontalLayout_56.addWidget(self.lblfoto2)

        self.lblfoto3 = QLabel(self.lytWeb)
        self.lblfoto3.setObjectName(u"lblfoto3")
        self.lblfoto3.setMinimumSize(QSize(0, 0))
        self.lblfoto3.setMaximumSize(QSize(400, 700))
        self.lblfoto3.setStyleSheet(u"border: 2px solid rgb(33, 37, 43);\n"
"border-radius: 5px;\n"
"")
        self.lblfoto3.setScaledContents(True)

        self.horizontalLayout_56.addWidget(self.lblfoto3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_56)

        self.stackedWidget.addWidget(self.lytWeb)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font14 = QFont()
        font14.setFamily(u"Montserrat")
        font14.setBold(False)
        font14.setItalic(False)
        self.creditsLabel.setFont(font14)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_32.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(11)
        self.cmbNombreSesion.setCurrentIndex(-1)
        self.cmbselecNivel.setCurrentIndex(-1)
        self.cmbIntensidad.setCurrentIndex(-1)
        self.btnImgNut1.setDefault(False)
        self.btnSubirDieta.setDefault(False)
        self.ntCmbRemitente.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"RESILIENCE", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Fortaleza Fisica y Mental", None))
        self.label_5.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Ocultar", None))
        self.btnRegistrarUsuario.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.btnReservaClase.setText(QCoreApplication.translate("MainWindow", u"Reservar", None))
        self.btnBuscarUsuario.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnRegistrarEmpleado.setText(QCoreApplication.translate("MainWindow", u"Empleado", None))
        self.btnNuevaSesion.setText(QCoreApplication.translate("MainWindow", u"Nueva Sesi\u00f3n", None))
        self.btnNotificacion.setText(QCoreApplication.translate("MainWindow", u"Notificaci\u00f3n", None))
        self.btnAtras.setText(QCoreApplication.translate("MainWindow", u"Atras", None))
        self.btnCerrarSesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesion", None))
        self.titleRightInfo.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.lblLogoReservar.setText("")
        self.txtNumCliente.setText("")
        self.txtNumCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero de Cliente", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.lblNumCliente.setText("")
        self.label_10.setText("")
        self.cmbHorario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione el nivel", None))
        self.btnReservarClase.setText(QCoreApplication.translate("MainWindow", u"Reservar", None))
        self.cmbClase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione Nombre y Hora de la sesi\u00f3n", None))
        self.lblFotoPerfil.setText("")
        self.lblLogoBuscar.setText("")
        self.lblBuscar.setText("")
        self.cmbOpcionRenovar.setCurrentText("")
        self.cmbOpcionRenovar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione una opci\u00f3n", None))
        self.lbluid.setText("")
        self.btnBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lblOpcionRenovar.setText(QCoreApplication.translate("MainWindow", u"Renovar suscripci\u00f3n No/Si", None))
        self.chkOpcionRenovar.setText("")
        self.btnRenovar.setText(QCoreApplication.translate("MainWindow", u"Renovar", None))
        self.txtBuscar.setText("")
        self.txtBuscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero de cliente", None))
        self.label.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"DATOS DEL CLIENTE", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"d", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"e", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"f", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"g", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"h", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"i", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"j", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"k", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"l", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"m", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"n", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Cliente", None));
        ___qtablewidgetitem16 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Correo", None));
        ___qtablewidgetitem18 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None));
        ___qtablewidgetitem19 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        ___qtablewidgetitem20 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Membres\u00eda", None));
        ___qtablewidgetitem21 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        ___qtablewidgetitem22 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Estatura", None));
        ___qtablewidgetitem23 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Sexo", None));
        ___qtablewidgetitem24 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Sesiones", None));
        ___qtablewidgetitem25 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Valoraciones", None));
        ___qtablewidgetitem26 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Nutri\u00f3logo", None));
        ___qtablewidgetitem27 = self.tableWidget.item(12, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Nivel", None));
        ___qtablewidgetitem28 = self.tableWidget.item(13, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Vigencia", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem29 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"SESI\u00d3N", None));
        ___qtablewidgetitem30 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"FECHA", None));
        ___qtablewidgetitem31 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"HORA", None));
        self.label_2.setText("")
        self.lblLogoRegistro_2.setText("")
        self.label_25.setText("")
        self.txtNombreEmpleado.setInputMask("")
        self.txtNombreEmpleado.setText("")
        self.txtNombreEmpleado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_26.setText("")
        self.lblNombre_2.setText("")
        self.label_46.setText("")
        self.txtApellidoEmpleado.setText("")
        self.txtApellidoEmpleado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.label_47.setText("")
        self.lblApellido_2.setText("")
        self.label_7.setText("")
        self.cmbTipoEmpleado.setItemText(0, QCoreApplication.translate("MainWindow", u"Entrenador", None))
        self.cmbTipoEmpleado.setItemText(1, QCoreApplication.translate("MainWindow", u"Nutri\u00f3logo", None))
        self.cmbTipoEmpleado.setItemText(2, QCoreApplication.translate("MainWindow", u"Recepcionista", None))

        self.cmbTipoEmpleado.setCurrentText("")
        self.cmbTipoEmpleado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione tipo de empleado", None))
        self.label_27.setText("")
        self.lblCorreo_2.setText("")
        self.label_31.setText("")
        self.txtContrasenaEmpleado.setText("")
        self.txtContrasenaEmpleado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_28.setText("")
        self.lblTelefono_2.setText("")
        self.label_32.setText("")
        self.txtRepetirContrasena.setText("")
        self.txtRepetirContrasena.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repetir Contrase\u00f1a", None))
        self.label_33.setText("")
        self.lblEdad_2.setText("")
        self.label_56.setText("")
        self.label_57.setText("")
        self.lblTipoMembresia_2.setText("")
        self.btnRegistroEmpleado.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.lblRegistrarEmpleado.setText("")
        self.lblGuardar_2.setText("")
        self.lblLogoReservar_2.setText("")
        self.label_3.setText("")
        self.lblNuevaAgregar.setText("")
        self.btnAgregar_2.setText("")
        self.lblHora1.setText("")
        self.label_11.setText("")
        self.lblHora2.setText("")
        self.lblFechaAgregar.setText("")
        self.txtFechaAgregar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha (mm-dd-aaaa)", None))
        self.txtHoraAgregar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hora (hh:mm)", None))
        self.pushButton.setText("")
        self.lblNivel_2.setText("")
        ___qtablewidgetitem32 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem33 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem34 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Intensidad", None));
        ___qtablewidgetitem35 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Nivel", None));
        ___qtablewidgetitem36 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        self.cmbNombreSesion.setCurrentText("")
        self.cmbNombreSesion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de sesi\u00f3n", None))
        self.lblHoraAgregar.setText("")
        self.txtNuevaAgregar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nuevo nombre de sesi\u00f3n", None))
        self.label_37.setText("")
        self.lblNivel.setText("")
        self.lblHora3.setText("")
        self.lblHora4.setText("")
        self.btnNuevaClase.setText("")
        self.cmbselecNivel.setCurrentText("")
        self.cmbselecNivel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione nivel", None))
        self.cmbIntensidad.setCurrentText("")
        self.cmbIntensidad.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecciona intensidad", None))
        self.txtUrlAgregar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.btnSubirLink.setText("")
        self.lblAgregar.setText("")
        self.btnAgregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_39.setText("")
        self.txtNClienteNut.setText("")
        self.txtNClienteNut.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero de cliente", None))
        self.btnBNut.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lblNClienteNut.setText("")
        self.label_36.setText("")
        ___qtablewidgetitem37 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"DATOS PERSONALES", None));
        ___qtablewidgetitem38 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Datos Personales", None));
        ___qtablewidgetitem39 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Plan", None));
        ___qtablewidgetitem40 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Objetivo", None));
        ___qtablewidgetitem41 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Dieta anterior", None));
        ___qtablewidgetitem42 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Realiza ejercicio", None));
        ___qtablewidgetitem43 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Nivel de ejercicio", None));
        ___qtablewidgetitem44 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Tipo ejercicico", None));
        ___qtablewidgetitem45 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Tiempo ejercicio", None));
        ___qtablewidgetitem46 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Horario ejercicio", None));
        ___qtablewidgetitem47 = self.tableWidget_3.verticalHeaderItem(9)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Es activo", None));
        ___qtablewidgetitem48 = self.tableWidget_3.verticalHeaderItem(10)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Enfermedades", None));
        ___qtablewidgetitem49 = self.tableWidget_3.verticalHeaderItem(11)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Mov. con dolor", None));
        ___qtablewidgetitem50 = self.tableWidget_3.verticalHeaderItem(12)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Tiene Material", None));
        ___qtablewidgetitem51 = self.tableWidget_3.verticalHeaderItem(13)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Medidas", None));
        ___qtablewidgetitem52 = self.tableWidget_3.verticalHeaderItem(14)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Cuello", None));
        ___qtablewidgetitem53 = self.tableWidget_3.verticalHeaderItem(15)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Cintura", None));
        ___qtablewidgetitem54 = self.tableWidget_3.verticalHeaderItem(16)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Abdomen", None));
        ___qtablewidgetitem55 = self.tableWidget_3.verticalHeaderItem(17)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Cadera", None));
        ___qtablewidgetitem56 = self.tableWidget_3.verticalHeaderItem(18)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Varias", None));

        __sortingEnabled1 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem57 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Plan", None));
        ___qtablewidgetitem58 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Objetivo", None));
        ___qtablewidgetitem59 = self.tableWidget_3.item(2, 0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Dieta Anterior", None));
        ___qtablewidgetitem60 = self.tableWidget_3.item(3, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Realiza Ejerciccio", None));
        ___qtablewidgetitem61 = self.tableWidget_3.item(4, 0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Nivel de ejercicio", None));
        ___qtablewidgetitem62 = self.tableWidget_3.item(5, 0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Tipo ejercicico", None));
        ___qtablewidgetitem63 = self.tableWidget_3.item(6, 0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Tiempo ejercicico", None));
        ___qtablewidgetitem64 = self.tableWidget_3.item(7, 0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Horario ejercicio", None));
        ___qtablewidgetitem65 = self.tableWidget_3.item(8, 0)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Es activo", None));
        ___qtablewidgetitem66 = self.tableWidget_3.item(9, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Enfermedades", None));
        ___qtablewidgetitem67 = self.tableWidget_3.item(10, 0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Mov. con dolor", None));
        ___qtablewidgetitem68 = self.tableWidget_3.item(11, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Tiene material", None));
        ___qtablewidgetitem69 = self.tableWidget_3.item(12, 0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Horas de dormir", None));
        ___qtablewidgetitem70 = self.tableWidget_3.item(13, 0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"MEDIDAS", None));
        ___qtablewidgetitem71 = self.tableWidget_3.item(14, 0)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Cuello", None));
        ___qtablewidgetitem72 = self.tableWidget_3.item(15, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Cintura", None));
        ___qtablewidgetitem73 = self.tableWidget_3.item(16, 0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Abdomen", None));
        ___qtablewidgetitem74 = self.tableWidget_3.item(17, 0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Cadera", None));
        ___qtablewidgetitem75 = self.tableWidget_3.item(18, 0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Varias", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem76 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"COMIDA", None));
        ___qtablewidgetitem77 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Comidas", None));
        ___qtablewidgetitem78 = self.tableWidget_4.verticalHeaderItem(1)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Horas de hambre", None));
        ___qtablewidgetitem79 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Desayunos preferidos", None));
        ___qtablewidgetitem80 = self.tableWidget_4.verticalHeaderItem(3)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Desayunos", None));
        ___qtablewidgetitem81 = self.tableWidget_4.verticalHeaderItem(4)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Comidas preferidas", None));
        ___qtablewidgetitem82 = self.tableWidget_4.verticalHeaderItem(5)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Comidas", None));
        ___qtablewidgetitem83 = self.tableWidget_4.verticalHeaderItem(6)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Cenas preferidas", None));
        ___qtablewidgetitem84 = self.tableWidget_4.verticalHeaderItem(7)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Cenas", None));
        ___qtablewidgetitem85 = self.tableWidget_4.verticalHeaderItem(8)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Preparacion de alimentos", None));
        ___qtablewidgetitem86 = self.tableWidget_4.verticalHeaderItem(9)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Comida facil de llevar", None));
        ___qtablewidgetitem87 = self.tableWidget_4.verticalHeaderItem(10)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Verduras y frutas favoritas", None));
        ___qtablewidgetitem88 = self.tableWidget_4.verticalHeaderItem(11)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Frutas", None));

        __sortingEnabled2 = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        ___qtablewidgetitem89 = self.tableWidget_4.item(0, 0)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Horas de hambre", None));
        ___qtablewidgetitem90 = self.tableWidget_4.item(1, 0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Desayunos preferidos", None));
        ___qtablewidgetitem91 = self.tableWidget_4.item(2, 0)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Desayunos", None));
        ___qtablewidgetitem92 = self.tableWidget_4.item(3, 0)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Comidas preferidas", None));
        ___qtablewidgetitem93 = self.tableWidget_4.item(4, 0)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Comidas", None));
        ___qtablewidgetitem94 = self.tableWidget_4.item(5, 0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Cenas preferidas", None));
        ___qtablewidgetitem95 = self.tableWidget_4.item(6, 0)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Cenas", None));
        ___qtablewidgetitem96 = self.tableWidget_4.item(7, 0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Preparaci\u00f3n de alimentos", None));
        ___qtablewidgetitem97 = self.tableWidget_4.item(8, 0)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Comida facil de llevar", None));
        ___qtablewidgetitem98 = self.tableWidget_4.item(9, 0)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Verduras y frutas favoritas", None));
        ___qtablewidgetitem99 = self.tableWidget_4.item(10, 0)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Frutas", None));
        ___qtablewidgetitem100 = self.tableWidget_4.item(11, 0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Verduras", None));
        self.tableWidget_4.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem101 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"COMIDA", None));
        ___qtablewidgetitem102 = self.tableWidget_5.verticalHeaderItem(0)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Frituras o dulces favoritos", None));
        ___qtablewidgetitem103 = self.tableWidget_5.verticalHeaderItem(1)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Alimentos que no le gustan", None));
        ___qtablewidgetitem104 = self.tableWidget_5.verticalHeaderItem(2)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Comida de fin de semana", None));
        ___qtablewidgetitem105 = self.tableWidget_5.verticalHeaderItem(3)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Lo que suele tomar", None));
        ___qtablewidgetitem106 = self.tableWidget_5.verticalHeaderItem(4)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Toma proteina", None));
        ___qtablewidgetitem107 = self.tableWidget_5.verticalHeaderItem(5)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Toma otro suplemento", None));
        ___qtablewidgetitem108 = self.tableWidget_5.verticalHeaderItem(6)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"Razon de comer", None));
        ___qtablewidgetitem109 = self.tableWidget_5.verticalHeaderItem(7)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"Toma medicamento", None));
        ___qtablewidgetitem110 = self.tableWidget_5.verticalHeaderItem(8)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Cocina en casa", None));
        ___qtablewidgetitem111 = self.tableWidget_5.verticalHeaderItem(9)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"Numero de comidas", None));
        ___qtablewidgetitem112 = self.tableWidget_5.verticalHeaderItem(10)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"Comer seguido lo mismo", None));
        ___qtablewidgetitem113 = self.tableWidget_5.verticalHeaderItem(11)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Alergico", None));
        ___qtablewidgetitem114 = self.tableWidget_5.verticalHeaderItem(12)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"Es de otro pais", None));

        __sortingEnabled3 = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        ___qtablewidgetitem115 = self.tableWidget_5.item(0, 0)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"Frituras o dulces favoritos", None));
        ___qtablewidgetitem116 = self.tableWidget_5.item(1, 0)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"Alimentos que no le gustan", None));
        ___qtablewidgetitem117 = self.tableWidget_5.item(2, 0)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"Comida de fin de semana", None));
        ___qtablewidgetitem118 = self.tableWidget_5.item(3, 0)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Lo que suele tomar", None));
        ___qtablewidgetitem119 = self.tableWidget_5.item(4, 0)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"Toma proteina", None));
        ___qtablewidgetitem120 = self.tableWidget_5.item(5, 0)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Toma otro suplemento", None));
        ___qtablewidgetitem121 = self.tableWidget_5.item(6, 0)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Razon de comer", None));
        ___qtablewidgetitem122 = self.tableWidget_5.item(7, 0)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Toma medicamento", None));
        ___qtablewidgetitem123 = self.tableWidget_5.item(8, 0)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"Cocina en casa", None));
        ___qtablewidgetitem124 = self.tableWidget_5.item(9, 0)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"Numero de comidas", None));
        ___qtablewidgetitem125 = self.tableWidget_5.item(10, 0)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"Comer seguido lo mismo", None));
        ___qtablewidgetitem126 = self.tableWidget_5.item(11, 0)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"Alergico", None));
        ___qtablewidgetitem127 = self.tableWidget_5.item(12, 0)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"Es de otro pais", None));
        self.tableWidget_5.setSortingEnabled(__sortingEnabled3)

        self.btnImgNut4.setText(QCoreApplication.translate("MainWindow", u"Ver Dieta", None))
        self.lblPersonalizado.setText(QCoreApplication.translate("MainWindow", u" PLAN PERSONALIZADO", None))
        self.btnImgNut1.setText(QCoreApplication.translate("MainWindow", u"Ver Fotos", None))
        self.cmbFechaImg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione Fecha", None))
        self.cmbSubirDieta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione plan", None))
        self.lblFotografias.setText(QCoreApplication.translate("MainWindow", u" FOTOGRAFIAS", None))
        self.btnSubirDieta.setText(QCoreApplication.translate("MainWindow", u"Subir Dieta", None))
        self.lblAbrirImg.setText("")
        self.lblFileName.setText("")
        self.label_17.setText("")
        self.lblImgDieta.setText("")
        self.txtNClientePsi.setText("")
        self.txtNClientePsi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero de Cliente", None))
        self.btnBPsi.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lblNClientePsi.setText("")
        self.btnCSPsi.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesi\u00f3n", None))
        self.lblNClienteEnt.setText("")
        self.txtNClienteEnt.setText("")
        self.txtNClienteEnt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero de Cliente", None))
        self.btnBEnt.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnCSEnt.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesi\u00f3n", None))
        self.lblLogoReservar_5.setText("")
        self.ntTxtTexto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Texto", None))
        self.ntCmbRemitente.setCurrentText("")
        self.ntCmbRemitente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione a quien se le enviar\u00e1", None))
        self.ntTxtNumCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero de Cliente", None))
        self.ntBtnEnviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.ntTxtTitulo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.ntLblCmbRemitente.setText("")
        self.ntLblTexto.setText("")
        self.ntLblUrl.setText("")
        self.ntLblBtnEnviar.setText("")
        self.ntLblTitulo.setText("")
        self.lblLogoLogin.setText("")
        self.label_35.setText("")
        self.label_22.setText("")
        self.txtUsuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_6.setText("")
        self.txtContrasea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_43.setText("")
        self.label_42.setText("")
        self.label_14.setText("")
        self.label_40.setText("")
        self.label_41.setText("")
        self.label_18.setText("")
        self.cmbTipoDeUsuario.setItemText(0, QCoreApplication.translate("MainWindow", u"Entrenador", None))
        self.cmbTipoDeUsuario.setItemText(1, QCoreApplication.translate("MainWindow", u"Nutri\u00f3logo", None))
        self.cmbTipoDeUsuario.setItemText(2, QCoreApplication.translate("MainWindow", u"Recepcionista", None))

        self.cmbTipoDeUsuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione un tipo de usuario", None))
        self.btnIniciarSesion.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesi\u00f3n", None))
        self.lblLogoRegistro.setText("")
        self.label_23.setText("")
        self.txtNombre.setInputMask("")
        self.txtNombre.setText("")
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_19.setText("")
        self.lblNombre.setText("")
        self.label_44.setText("")
        self.txtApellido.setText("")
        self.txtApellido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.label_45.setText("")
        self.lblApellido.setText("")
        self.label_4.setText("")
        self.txtCorreo.setText("")
        self.txtCorreo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_20.setText("")
        self.lblCorreo.setText("")
        self.label_29.setText("")
        self.txtTelefono.setText("")
        self.txtTelefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.label_21.setText("")
        self.lblTelefono.setText("")
        self.label_30.setText("")
        self.txtEdad.setText("")
        self.txtEdad.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Edad", None))
        self.txtAltura.setText("")
        self.txtAltura.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Estatura", None))
        self.txtPeso.setText("")
        self.txtPeso.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.label_24.setText("")
        self.label_13.setText("")
        self.lblEdad.setText("")
        self.lblEstatura.setText("")
        self.lblPeso.setText("")
        self.label_15.setText("")
        self.label_54.setText("")
        self.cmbTipoSexo.setItemText(0, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.cmbTipoSexo.setItemText(1, QCoreApplication.translate("MainWindow", u"Femenino", None))

        self.cmbTipoSexo.setCurrentText("")
        self.cmbTipoSexo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione sexo", None))
        self.label_55.setText("")
        self.lblTipoMembresia.setText("")
        self.label_58.setText("")
        self.cmbNivel.setCurrentText("")
        self.cmbNivel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione nivel", None))
        self.label_59.setText("")
        self.lblTipoMembresia_3.setText("")
        self.btnRegistrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.lblRegistrar.setText("")
        self.lblfoto1.setText("")
        self.lblfoto2.setText("")
        self.lblfoto3.setText("")
        self.creditsLabel.setText("")
        self.version.setText("")
    # retranslateUi

