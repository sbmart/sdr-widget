{'application':{'type':'Application',
          'name':'Widget Control',
    'backgrounds': [
    {'type':'Background',
          'name':'bgControlMobo',
          'title':'Widget Control Tool',
          'size':(922, 573),

         'components': [

{'type':'StaticText', 
    'name':'BoardType', 
    'position':(50, 200),
    'size':(175,-1),
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'Board Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxBoard', 
    'position':(40, 250), 
    'size':(100, -1), 
    'items':[u'none', u'widget', u'usbi2s', u'usbdac', u'test'], 
    'stringSelection':'widget', 
    'text':'board', 
    },


{'type':'StaticText', 
    'name':'ImageType', 
    'position':(150, 200),
    'size':(175,-1),
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'Image Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxImage', 
    'position':(145, 250), 
    'size':(135, -1), 
    'items':[u'flashyblinky', u'uac1_audio', u'uac1_dg8saq', u'uac2_audio', u'uac2_dg8saq', u'hpsdr', u'test'], 
    'stringSelection':'uac1_dg8saq', 
    'text':'Image', 
    },


{'type':'StaticText', 
    'name':'InType', 
    'position':(300, 200),
    'size':(175,-1),
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'IN Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxIn', 
    'position':(295, 250), 
    'size':(100, -1), 
    'items':[u'normal', u'swapped'], 
    'stringSelection':'Normal', 
    'text':'IN Type', 
    },


{'type':'StaticText', 
    'name':'OutType', 
    'position':(400, 200),
    'size':(175,-1),
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'OUT Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxOut', 
    'position':(395, 250), 
    'size':(100, -1), 
    'items':[u'normal', u'swapped'], 
    'stringSelection':'normal', 
    'text':'OUT Type', 
    },


{'type':'StaticText', 
    'name':'AdcType', 
    'position':(550, 200),
    'size':(175,-1),
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'ADC Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxAdc', 
    'position':(525, 250), 
    'size':(100, -1), 
    'items':[u'none', u'ak5394a'], 
    'stringSelection':'ak5394a', 
    'text':'ADC Type', 
    },


{'type':'StaticText', 
    'name':'DacType', 
    'position':(675, 200),
    'size':(175,-1),
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'DAC Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxDac', 
    'position':(650, 250), 
    'size':(100, -1), 
    'items':[u'none', u'cs4344', u'es9022'], 
    'stringSelection':'cs4344', 
    'text':'DAC Type', 
    },

{'type':'StaticText', 
    'name':'LCDType', 
    'position':(800, 200),
    'size':(175,-1),
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'LCD Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxLCD', 
    'position':(780, 250), 
    'size':(100, -1), 
    'items':[u'none', u'hd44780', u'ks0073'], 
    'stringSelection':'hd44780', 
    'text':'LCD Type', 
    },

{'type':'StaticText', 
    'name':'LogType', 
    'position':(50, 350),
    'size':(175,-1),
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'Log Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxLog', 
    'position':(40, 400), 
    'size':(100, -1), 
    'items':[u'none', u'1sec', u'2sec', u'4sec'], 
    'stringSelection':'widget', 
    'text':'log', 
    },



{'type':'StaticBox', 
    'name':'readFromFirmware', 
    'position':(14, 522), 
    'size':(175, 43), 
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Read From Firmware', 
    },


{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(637, 343), 
    'size':(98, 90), 
    'alignment':'center', 
    'backgroundColor':(240, 235, 226), 
    'font':{'style': 'bold', 'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 16}, 
    'text':'Control Widget', 
    },

{'type':'StaticBox', 
    'name':'staticboxFirmware', 
    'position':(726, 479), 
    'size':(175, 86), 
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Firmware Control', 
    },

{'type':'StaticText', 
    'name':'FirmwareSdisplay', 
    'position':(805, 500), 
    'size':(87, -1), 
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'text':'FirmwareSdisplay', 
    },

{'type':'StaticText', 
    'name':'serialNumber', 
    'position':(733, 499), 
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'text':'Serial Number:', 
    },

{'type':'StaticText', 
    'name':'FirmwareVdisplay', 
    'position':(805, 520), 
    'size':(87, -1), 
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'text':'FirmwareVdisplay', 
    },

{'type':'StaticText', 
    'name':'stFirmwareV', 
    'position':(733, 519), 
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'text':'Version........:', 
    },

{'type':'StaticLine', 
    'name':'StaticLine11', 
    'position':(387, 430), 
    'size':(107, -1), 
    'backgroundColor':(240, 235, 226), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(387, 344), 
    'size':(107, -1), 
    'backgroundColor':(240, 235, 226), 
    'layout':'horizontal', 
    },


{'type':'StaticText', 
    'name':'stAuthor', 
    'position':(245, 543), 
    'size':(82, 22), 
    'alignment':'center', 
    'backgroundColor':(240, 235, 226), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 6}, 
    'text':'V 001 2011-03-11 9V1AL', 
    },


{'type':'Image', 
    'name':'Image1', 
    'position':(659, 10), 
    'size':(245, 156), 
    'backgroundColor':(240, 235, 226), 
    'file':'Po_SWR_board_beta.JPG', 
    },

{'type':'Button', 
    'name':'btnReset', 
    'position':(516, 538), 
    'size':(86, 25), 
    'command':'btnReset', 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Reset', 
    },

{'type':'Button', 
    'name':'btnFactoryReset', 
    'position':(624, 538), 
    'size':(86, 25), 
    'command':'btnFactoryReset', 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Factory Reset', 
    },

{'type':'Button', 
    'name':'btnStartUSB', 
    'position':(732, 538), 
    'size':(75, 25), 
    'command':'USB', 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Start USB', 
    },


{'type':'Button', 
    'name':'btnRefresh', 
    'position':(21, 538), 
    'size':(75, 25), 
    'command':'Refresh', 
    'default':1, 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Read', 
    },

{'type':'Button', 
    'name':'btnQuit', 
    'position':(821, 538), 
    'size':(75, 25), 
    'command':'Exit', 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Quit', 
    },



] # end components
} # end background
] # end backgrounds
} }
