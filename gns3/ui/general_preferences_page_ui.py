# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/general_preferences_page.ui'
#
# Created: Sun Aug 31 14:07:13 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GeneralPreferencesPageWidget(object):
    def setupUi(self, GeneralPreferencesPageWidget):
        GeneralPreferencesPageWidget.setObjectName(_fromUtf8("GeneralPreferencesPageWidget"))
        GeneralPreferencesPageWidget.resize(502, 555)
        self.verticalLayout = QtGui.QVBoxLayout(GeneralPreferencesPageWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiTabWidget = QtGui.QTabWidget(GeneralPreferencesPageWidget)
        self.uiTabWidget.setObjectName(_fromUtf8("uiTabWidget"))
        self.uiGeneralTab = QtGui.QWidget()
        self.uiGeneralTab.setObjectName(_fromUtf8("uiGeneralTab"))
        self.gridLayout_8 = QtGui.QGridLayout(self.uiGeneralTab)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.uiLocalPathsGroupBox = QtGui.QGroupBox(self.uiGeneralTab)
        self.uiLocalPathsGroupBox.setObjectName(_fromUtf8("uiLocalPathsGroupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.uiLocalPathsGroupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.uiProjectsPathLabel = QtGui.QLabel(self.uiLocalPathsGroupBox)
        self.uiProjectsPathLabel.setObjectName(_fromUtf8("uiProjectsPathLabel"))
        self.gridLayout_3.addWidget(self.uiProjectsPathLabel, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.uiProjectsPathLineEdit = QtGui.QLineEdit(self.uiLocalPathsGroupBox)
        self.uiProjectsPathLineEdit.setObjectName(_fromUtf8("uiProjectsPathLineEdit"))
        self.horizontalLayout_2.addWidget(self.uiProjectsPathLineEdit)
        self.uiProjectsPathToolButton = QtGui.QToolButton(self.uiLocalPathsGroupBox)
        self.uiProjectsPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiProjectsPathToolButton.setObjectName(_fromUtf8("uiProjectsPathToolButton"))
        self.horizontalLayout_2.addWidget(self.uiProjectsPathToolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.uiImagesPathLabel = QtGui.QLabel(self.uiLocalPathsGroupBox)
        self.uiImagesPathLabel.setObjectName(_fromUtf8("uiImagesPathLabel"))
        self.gridLayout_3.addWidget(self.uiImagesPathLabel, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.uiImagesPathLineEdit = QtGui.QLineEdit(self.uiLocalPathsGroupBox)
        self.uiImagesPathLineEdit.setObjectName(_fromUtf8("uiImagesPathLineEdit"))
        self.horizontalLayout_4.addWidget(self.uiImagesPathLineEdit)
        self.uiImagesPathToolButton = QtGui.QToolButton(self.uiLocalPathsGroupBox)
        self.uiImagesPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiImagesPathToolButton.setObjectName(_fromUtf8("uiImagesPathToolButton"))
        self.horizontalLayout_4.addWidget(self.uiImagesPathToolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.uiTemporaryFilesPathLabel = QtGui.QLabel(self.uiLocalPathsGroupBox)
        self.uiTemporaryFilesPathLabel.setObjectName(_fromUtf8("uiTemporaryFilesPathLabel"))
        self.gridLayout_3.addWidget(self.uiTemporaryFilesPathLabel, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.uiTemporaryFilesPathLineEdit = QtGui.QLineEdit(self.uiLocalPathsGroupBox)
        self.uiTemporaryFilesPathLineEdit.setObjectName(_fromUtf8("uiTemporaryFilesPathLineEdit"))
        self.horizontalLayout_3.addWidget(self.uiTemporaryFilesPathLineEdit)
        self.uiTemporaryFilesPathToolButton = QtGui.QToolButton(self.uiLocalPathsGroupBox)
        self.uiTemporaryFilesPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiTemporaryFilesPathToolButton.setObjectName(_fromUtf8("uiTemporaryFilesPathToolButton"))
        self.horizontalLayout_3.addWidget(self.uiTemporaryFilesPathToolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.gridLayout_8.addWidget(self.uiLocalPathsGroupBox, 0, 0, 1, 2)
        self.uiConfigurationFileGroupBox = QtGui.QGroupBox(self.uiGeneralTab)
        self.uiConfigurationFileGroupBox.setObjectName(_fromUtf8("uiConfigurationFileGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.uiConfigurationFileGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uiImportConfigurationFilePushButton = QtGui.QPushButton(self.uiConfigurationFileGroupBox)
        self.uiImportConfigurationFilePushButton.setObjectName(_fromUtf8("uiImportConfigurationFilePushButton"))
        self.horizontalLayout.addWidget(self.uiImportConfigurationFilePushButton)
        self.uiExportConfigurationFilePushButton = QtGui.QPushButton(self.uiConfigurationFileGroupBox)
        self.uiExportConfigurationFilePushButton.setObjectName(_fromUtf8("uiExportConfigurationFilePushButton"))
        self.horizontalLayout.addWidget(self.uiExportConfigurationFilePushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.uiConfigurationFileLabel = QtGui.QLabel(self.uiConfigurationFileGroupBox)
        self.uiConfigurationFileLabel.setObjectName(_fromUtf8("uiConfigurationFileLabel"))
        self.gridLayout.addWidget(self.uiConfigurationFileLabel, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_8.addWidget(self.uiConfigurationFileGroupBox, 1, 0, 1, 2)
        self.uiGeneralMiscGroupBox = QtGui.QGroupBox(self.uiGeneralTab)
        self.uiGeneralMiscGroupBox.setObjectName(_fromUtf8("uiGeneralMiscGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.uiGeneralMiscGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.uiCheckForUpdateCheckBox = QtGui.QCheckBox(self.uiGeneralMiscGroupBox)
        self.uiCheckForUpdateCheckBox.setChecked(True)
        self.uiCheckForUpdateCheckBox.setObjectName(_fromUtf8("uiCheckForUpdateCheckBox"))
        self.gridLayout_2.addWidget(self.uiCheckForUpdateCheckBox, 0, 0, 2, 2)
        self.uiSlowStartAllLabel = QtGui.QLabel(self.uiGeneralMiscGroupBox)
        self.uiSlowStartAllLabel.setObjectName(_fromUtf8("uiSlowStartAllLabel"))
        self.gridLayout_2.addWidget(self.uiSlowStartAllLabel, 3, 0, 1, 2)
        self.uiSlowStartAllSpinBox = QtGui.QSpinBox(self.uiGeneralMiscGroupBox)
        self.uiSlowStartAllSpinBox.setMaximum(10000)
        self.uiSlowStartAllSpinBox.setObjectName(_fromUtf8("uiSlowStartAllSpinBox"))
        self.gridLayout_2.addWidget(self.uiSlowStartAllSpinBox, 4, 0, 1, 2)
        self.uiLinkManualModeCheckBox = QtGui.QCheckBox(self.uiGeneralMiscGroupBox)
        self.uiLinkManualModeCheckBox.setChecked(True)
        self.uiLinkManualModeCheckBox.setObjectName(_fromUtf8("uiLinkManualModeCheckBox"))
        self.gridLayout_2.addWidget(self.uiLinkManualModeCheckBox, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.uiGeneralMiscGroupBox, 2, 0, 1, 2)
        self.uiRestoreDefaultsPushButton = QtGui.QPushButton(self.uiGeneralTab)
        self.uiRestoreDefaultsPushButton.setObjectName(_fromUtf8("uiRestoreDefaultsPushButton"))
        self.gridLayout_8.addWidget(self.uiRestoreDefaultsPushButton, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(324, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 4, 0, 1, 2)
        self.uiTabWidget.addTab(self.uiGeneralTab, _fromUtf8(""))
        self.uiConsoleTab = QtGui.QWidget()
        self.uiConsoleTab.setObjectName(_fromUtf8("uiConsoleTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.uiConsoleTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.uiTelnetConsoleSettingsGroupBox = QtGui.QGroupBox(self.uiConsoleTab)
        self.uiTelnetConsoleSettingsGroupBox.setObjectName(_fromUtf8("uiTelnetConsoleSettingsGroupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.uiTelnetConsoleSettingsGroupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.uiTelnetConsolePreconfiguredCommandLabel = QtGui.QLabel(self.uiTelnetConsoleSettingsGroupBox)
        self.uiTelnetConsolePreconfiguredCommandLabel.setObjectName(_fromUtf8("uiTelnetConsolePreconfiguredCommandLabel"))
        self.gridLayout_4.addWidget(self.uiTelnetConsolePreconfiguredCommandLabel, 0, 0, 1, 1)
        self.uiTelnetConsolePreconfiguredCommandComboBox = QtGui.QComboBox(self.uiTelnetConsoleSettingsGroupBox)
        self.uiTelnetConsolePreconfiguredCommandComboBox.setObjectName(_fromUtf8("uiTelnetConsolePreconfiguredCommandComboBox"))
        self.gridLayout_4.addWidget(self.uiTelnetConsolePreconfiguredCommandComboBox, 1, 0, 1, 1)
        self.uiTelnetConsoleCommandLabel = QtGui.QLabel(self.uiTelnetConsoleSettingsGroupBox)
        self.uiTelnetConsoleCommandLabel.setObjectName(_fromUtf8("uiTelnetConsoleCommandLabel"))
        self.gridLayout_4.addWidget(self.uiTelnetConsoleCommandLabel, 3, 0, 1, 1)
        self.uiTelnetConsoleCommandLineEdit = QtGui.QLineEdit(self.uiTelnetConsoleSettingsGroupBox)
        self.uiTelnetConsoleCommandLineEdit.setObjectName(_fromUtf8("uiTelnetConsoleCommandLineEdit"))
        self.gridLayout_4.addWidget(self.uiTelnetConsoleCommandLineEdit, 4, 0, 1, 2)
        self.uiTelnetConsolePreconfiguredCommandPushButton = QtGui.QPushButton(self.uiTelnetConsoleSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTelnetConsolePreconfiguredCommandPushButton.sizePolicy().hasHeightForWidth())
        self.uiTelnetConsolePreconfiguredCommandPushButton.setSizePolicy(sizePolicy)
        self.uiTelnetConsolePreconfiguredCommandPushButton.setObjectName(_fromUtf8("uiTelnetConsolePreconfiguredCommandPushButton"))
        self.gridLayout_4.addWidget(self.uiTelnetConsolePreconfiguredCommandPushButton, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.uiTelnetConsoleSettingsGroupBox)
        self.uiSerialConsoleSettingsGroupBox = QtGui.QGroupBox(self.uiConsoleTab)
        self.uiSerialConsoleSettingsGroupBox.setObjectName(_fromUtf8("uiSerialConsoleSettingsGroupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.uiSerialConsoleSettingsGroupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.uiSerialConsoleCommandLabel = QtGui.QLabel(self.uiSerialConsoleSettingsGroupBox)
        self.uiSerialConsoleCommandLabel.setObjectName(_fromUtf8("uiSerialConsoleCommandLabel"))
        self.gridLayout_5.addWidget(self.uiSerialConsoleCommandLabel, 3, 0, 1, 1)
        self.uiSerialConsolePreconfiguredCommandLabel = QtGui.QLabel(self.uiSerialConsoleSettingsGroupBox)
        self.uiSerialConsolePreconfiguredCommandLabel.setObjectName(_fromUtf8("uiSerialConsolePreconfiguredCommandLabel"))
        self.gridLayout_5.addWidget(self.uiSerialConsolePreconfiguredCommandLabel, 0, 0, 1, 1)
        self.uiSerialConsolePreconfiguredCommandComboBox = QtGui.QComboBox(self.uiSerialConsoleSettingsGroupBox)
        self.uiSerialConsolePreconfiguredCommandComboBox.setObjectName(_fromUtf8("uiSerialConsolePreconfiguredCommandComboBox"))
        self.gridLayout_5.addWidget(self.uiSerialConsolePreconfiguredCommandComboBox, 1, 0, 1, 1)
        self.uiSerialConsoleCommandLineEdit = QtGui.QLineEdit(self.uiSerialConsoleSettingsGroupBox)
        self.uiSerialConsoleCommandLineEdit.setObjectName(_fromUtf8("uiSerialConsoleCommandLineEdit"))
        self.gridLayout_5.addWidget(self.uiSerialConsoleCommandLineEdit, 4, 0, 1, 2)
        self.uiSerialConsolePreconfiguredCommandPushButton = QtGui.QPushButton(self.uiSerialConsoleSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSerialConsolePreconfiguredCommandPushButton.sizePolicy().hasHeightForWidth())
        self.uiSerialConsolePreconfiguredCommandPushButton.setSizePolicy(sizePolicy)
        self.uiSerialConsolePreconfiguredCommandPushButton.setObjectName(_fromUtf8("uiSerialConsolePreconfiguredCommandPushButton"))
        self.gridLayout_5.addWidget(self.uiSerialConsolePreconfiguredCommandPushButton, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.uiSerialConsoleSettingsGroupBox)
        self.uiConsoleMiscGroupBox = QtGui.QGroupBox(self.uiConsoleTab)
        self.uiConsoleMiscGroupBox.setObjectName(_fromUtf8("uiConsoleMiscGroupBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.uiConsoleMiscGroupBox)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.uiCloseConsoleWindowsOnDeleteCheckBox = QtGui.QCheckBox(self.uiConsoleMiscGroupBox)
        self.uiCloseConsoleWindowsOnDeleteCheckBox.setObjectName(_fromUtf8("uiCloseConsoleWindowsOnDeleteCheckBox"))
        self.gridLayout_7.addWidget(self.uiCloseConsoleWindowsOnDeleteCheckBox, 0, 0, 1, 1)
        self.uiBringConsoleWindowToFrontCheckBox = QtGui.QCheckBox(self.uiConsoleMiscGroupBox)
        self.uiBringConsoleWindowToFrontCheckBox.setObjectName(_fromUtf8("uiBringConsoleWindowToFrontCheckBox"))
        self.gridLayout_7.addWidget(self.uiBringConsoleWindowToFrontCheckBox, 1, 0, 1, 1)
        self.uiSlowConsoleAllLabel = QtGui.QLabel(self.uiConsoleMiscGroupBox)
        self.uiSlowConsoleAllLabel.setObjectName(_fromUtf8("uiSlowConsoleAllLabel"))
        self.gridLayout_7.addWidget(self.uiSlowConsoleAllLabel, 2, 0, 1, 1)
        self.uiSlowConsoleAllDoubleSpinBox = QtGui.QDoubleSpinBox(self.uiConsoleMiscGroupBox)
        self.uiSlowConsoleAllDoubleSpinBox.setDecimals(1)
        self.uiSlowConsoleAllDoubleSpinBox.setMinimum(0.0)
        self.uiSlowConsoleAllDoubleSpinBox.setSingleStep(0.5)
        self.uiSlowConsoleAllDoubleSpinBox.setProperty("value", 1.0)
        self.uiSlowConsoleAllDoubleSpinBox.setObjectName(_fromUtf8("uiSlowConsoleAllDoubleSpinBox"))
        self.gridLayout_7.addWidget(self.uiSlowConsoleAllDoubleSpinBox, 3, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.uiConsoleMiscGroupBox)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.uiTabWidget.addTab(self.uiConsoleTab, _fromUtf8(""))
        self.uiSceneTab = QtGui.QWidget()
        self.uiSceneTab.setObjectName(_fromUtf8("uiSceneTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.uiSceneTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.uiSceneWidthLabel = QtGui.QLabel(self.uiSceneTab)
        self.uiSceneWidthLabel.setObjectName(_fromUtf8("uiSceneWidthLabel"))
        self.verticalLayout_2.addWidget(self.uiSceneWidthLabel)
        self.uiSceneWidthSpinBox = QtGui.QSpinBox(self.uiSceneTab)
        self.uiSceneWidthSpinBox.setMinimum(500)
        self.uiSceneWidthSpinBox.setMaximum(1000000)
        self.uiSceneWidthSpinBox.setSingleStep(100)
        self.uiSceneWidthSpinBox.setProperty("value", 2000)
        self.uiSceneWidthSpinBox.setObjectName(_fromUtf8("uiSceneWidthSpinBox"))
        self.verticalLayout_2.addWidget(self.uiSceneWidthSpinBox)
        self.uiSceneHeightLabel = QtGui.QLabel(self.uiSceneTab)
        self.uiSceneHeightLabel.setObjectName(_fromUtf8("uiSceneHeightLabel"))
        self.verticalLayout_2.addWidget(self.uiSceneHeightLabel)
        self.uiSceneHeightSpinBox = QtGui.QSpinBox(self.uiSceneTab)
        self.uiSceneHeightSpinBox.setMinimum(500)
        self.uiSceneHeightSpinBox.setMaximum(1000000)
        self.uiSceneHeightSpinBox.setSingleStep(100)
        self.uiSceneHeightSpinBox.setProperty("value", 1000)
        self.uiSceneHeightSpinBox.setObjectName(_fromUtf8("uiSceneHeightSpinBox"))
        self.verticalLayout_2.addWidget(self.uiSceneHeightSpinBox)
        self.uiRectangleSelectedItemCheckBox = QtGui.QCheckBox(self.uiSceneTab)
        self.uiRectangleSelectedItemCheckBox.setChecked(True)
        self.uiRectangleSelectedItemCheckBox.setObjectName(_fromUtf8("uiRectangleSelectedItemCheckBox"))
        self.verticalLayout_2.addWidget(self.uiRectangleSelectedItemCheckBox)
        self.uiDrawLinkStatusPointsCheckBox = QtGui.QCheckBox(self.uiSceneTab)
        self.uiDrawLinkStatusPointsCheckBox.setChecked(True)
        self.uiDrawLinkStatusPointsCheckBox.setObjectName(_fromUtf8("uiDrawLinkStatusPointsCheckBox"))
        self.verticalLayout_2.addWidget(self.uiDrawLinkStatusPointsCheckBox)
        self.uiLabelPreviewLabel = QtGui.QLabel(self.uiSceneTab)
        self.uiLabelPreviewLabel.setObjectName(_fromUtf8("uiLabelPreviewLabel"))
        self.verticalLayout_2.addWidget(self.uiLabelPreviewLabel)
        self.uiDefaultLabelStylePlainTextEdit = QtGui.QPlainTextEdit(self.uiSceneTab)
        self.uiDefaultLabelStylePlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.uiDefaultLabelStylePlainTextEdit.setReadOnly(True)
        self.uiDefaultLabelStylePlainTextEdit.setObjectName(_fromUtf8("uiDefaultLabelStylePlainTextEdit"))
        self.verticalLayout_2.addWidget(self.uiDefaultLabelStylePlainTextEdit)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.uiDefaultLabelFontPushButton = QtGui.QPushButton(self.uiSceneTab)
        self.uiDefaultLabelFontPushButton.setObjectName(_fromUtf8("uiDefaultLabelFontPushButton"))
        self.horizontalLayout_5.addWidget(self.uiDefaultLabelFontPushButton)
        self.uiDefaultLabelColorPushButton = QtGui.QPushButton(self.uiSceneTab)
        self.uiDefaultLabelColorPushButton.setObjectName(_fromUtf8("uiDefaultLabelColorPushButton"))
        self.horizontalLayout_5.addWidget(self.uiDefaultLabelColorPushButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtGui.QSpacerItem(20, 201, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.uiTabWidget.addTab(self.uiSceneTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.uiTabWidget)

        self.retranslateUi(GeneralPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GeneralPreferencesPageWidget)

    def retranslateUi(self, GeneralPreferencesPageWidget):
        GeneralPreferencesPageWidget.setWindowTitle(_translate("GeneralPreferencesPageWidget", "General", None))
        self.uiLocalPathsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Local paths", None))
        self.uiProjectsPathLabel.setText(_translate("GeneralPreferencesPageWidget", "My projects:", None))
        self.uiProjectsPathLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "Directory where your GNS3 projects are stored", None))
        self.uiProjectsPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "...", None))
        self.uiImagesPathLabel.setText(_translate("GeneralPreferencesPageWidget", "My binary images:", None))
        self.uiImagesPathLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "Directory where your binary images (e.g. IOS) are stored", None))
        self.uiImagesPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "...", None))
        self.uiTemporaryFilesPathLabel.setText(_translate("GeneralPreferencesPageWidget", "Temporary files:", None))
        self.uiTemporaryFilesPathLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "Directory where temporary files are stored", None))
        self.uiTemporaryFilesPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "...", None))
        self.uiConfigurationFileGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Configuration file", None))
        self.uiImportConfigurationFilePushButton.setText(_translate("GeneralPreferencesPageWidget", "&Import", None))
        self.uiExportConfigurationFilePushButton.setText(_translate("GeneralPreferencesPageWidget", "&Export", None))
        self.uiConfigurationFileLabel.setText(_translate("GeneralPreferencesPageWidget", "Unknown location", None))
        self.uiGeneralMiscGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Miscellaneous", None))
        self.uiCheckForUpdateCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Automatically check for update", None))
        self.uiSlowStartAllLabel.setText(_translate("GeneralPreferencesPageWidget", "Delay between each device start when starting all devices:", None))
        self.uiSlowStartAllSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " seconds", None))
        self.uiLinkManualModeCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Always use manual mode when adding links", None))
        self.uiRestoreDefaultsPushButton.setText(_translate("GeneralPreferencesPageWidget", "Restore defaults", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiGeneralTab), _translate("GeneralPreferencesPageWidget", "General", None))
        self.uiTelnetConsoleSettingsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Console settings for Telnet connections", None))
        self.uiTelnetConsolePreconfiguredCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Preconfigured commands:", None))
        self.uiTelnetConsoleCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Console application command:", None))
        self.uiTelnetConsoleCommandLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "<html><head/><body><p>Command line replacements:</p><p>%h = device server </p><p>%p = device port</p><p>%d = device hostname</p></body></html>", None))
        self.uiTelnetConsolePreconfiguredCommandPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Set", None))
        self.uiSerialConsoleSettingsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Console settings for local serial connections", None))
        self.uiSerialConsoleCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Console application command:", None))
        self.uiSerialConsolePreconfiguredCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Preconfigured commands:", None))
        self.uiSerialConsoleCommandLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "<html><head/><body><p>Command line replacements:</p><p>%d = device hostname</p><p>%s = device pipe file</p></body></html>", None))
        self.uiSerialConsolePreconfiguredCommandPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Set", None))
        self.uiConsoleMiscGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Miscellaneous", None))
        self.uiCloseConsoleWindowsOnDeleteCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Close any connected console window when deleting a node", None))
        self.uiBringConsoleWindowToFrontCheckBox.setToolTip(_translate("GeneralPreferencesPageWidget", "<html>This option will attempt to bring existing opened console window to front, instead of opening a new window.<br>If no existing opened console window exists, it will start a new  console window.</html>", None))
        self.uiBringConsoleWindowToFrontCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Bring console window to front (experimental feature)", None))
        self.uiSlowConsoleAllLabel.setText(_translate("GeneralPreferencesPageWidget", "Delay between each console launch when consoling to all devices:", None))
        self.uiSlowConsoleAllDoubleSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " seconds", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiConsoleTab), _translate("GeneralPreferencesPageWidget", "Console applications", None))
        self.uiSceneWidthLabel.setText(_translate("GeneralPreferencesPageWidget", "Default width:", None))
        self.uiSceneWidthSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " pixels", None))
        self.uiSceneHeightLabel.setText(_translate("GeneralPreferencesPageWidget", "Default height:", None))
        self.uiSceneHeightSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " pixels", None))
        self.uiRectangleSelectedItemCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Draw a rectangle when an item is selected", None))
        self.uiDrawLinkStatusPointsCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Draw link status points", None))
        self.uiLabelPreviewLabel.setText(_translate("GeneralPreferencesPageWidget", "Default label style:", None))
        self.uiDefaultLabelStylePlainTextEdit.setPlainText(_translate("GeneralPreferencesPageWidget", "AaBbYyZz", None))
        self.uiDefaultLabelFontPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Select default font", None))
        self.uiDefaultLabelColorPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Select default color", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiSceneTab), _translate("GeneralPreferencesPageWidget", "Topology view", None))

