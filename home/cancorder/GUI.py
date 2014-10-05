import wx
import MySQLdb as mdb
import sys
import time
import datetime

global PhaseAtempValue;
global BusVoltageValue;
global MotorIdValue;
global MotorTempValue;
global MotorVelocityValue;
global PackTempValue;
global PackSOCValue;
global PackBalanceValue;
global PrechargeContValue;
global MainContValue;
global EStopValue;
global END;
 

class MainFrame(wx.Frame):
           
    def __init__(self, parent, id):
        wx.Frame.__init__(self, None, title = 'CANSim')
        
        self.InitUI()
        
    def InitUI(self):
        MainPanel = wx.Panel(self)

        #Create Vertical Slider for BusVoltage
        BusVoltage = wx.Slider(MainPanel, value=375, minValue=100, maxValue=500, pos=(50, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        BusVoltage.Bind(wx.EVT_SCROLL, self.OnSliderScrollBV)

        #create labels for BusVoltage Slider
        self.BusVoltageTxt  = wx.StaticText(MainPanel, label='375', pos=(52, 33))
        self.BusVoltageTxt2 = wx.StaticText(MainPanel, label='BusVoltage',pos=(30,300))

######################################################################################################################
        
        #Create Vertical Slider for PhaseAtemp
        PhaseAtemp = wx.Slider(MainPanel, value=375, minValue=100, maxValue=500, pos=(200, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        PhaseAtemp.Bind(wx.EVT_SCROLL, self.OnSliderScrollPA)

        #create labels for PhaseAtemp Slider
        self.PhaseAtempTxt  = wx.StaticText(MainPanel, label='375', pos=(202, 33))
        self.PhaseAtempTxt2 = wx.StaticText(MainPanel, label='PhaseAtemp',pos=(180,300))
        
######################################################################################################################      

        #Create Vertical Slider for MotorId
        MotorId = wx.Slider(MainPanel, value=375, minValue=100, maxValue=500, pos=(350, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        MotorId.Bind(wx.EVT_SCROLL, self.OnSliderScrollMI)
        
        #create lables for MotorId Slider
        self.MotorIdTxt  = wx.StaticText(MainPanel, label='375', pos=(352,33))
        self.MotorIdTxt2 = wx.StaticText(MainPanel, label='MotorId', pos=(330,300))

######################################################################################################################

        #Create vertical slider for MotorTemp
        MotorTemp = wx.Slider(MainPanel, value=375, minValue=100, maxValue=500, pos=(500, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        MotorTemp.Bind(wx.EVT_SCROLL, self.OnSliderScrollMT)

        #create lables for MotorTemp Slider
        self.MotorTempTxt  = wx.StaticText(MainPanel, label='375', pos=(502,33))
        self.MotorTempTxt2 = wx.StaticText(MainPanel, label='MotorTemp', pos=(480,300))

#####################################################################################################################

        #Create vertical slider for MotorVelocity
        MotorVelocity = wx.Slider(MainPanel, value=375, minValue=100, maxValue=500, pos=(650, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        MotorVelocity.Bind(wx.EVT_SCROLL, self.OnSliderScrollMV)

        #create lables for MotorVelocity Slider
        self.MotorVelocityTxt  = wx.StaticText(MainPanel, label='375', pos=(652,33))
        self.MotorVelocityTxt2 = wx.StaticText(MainPanel, label='MotorVelocity', pos=(630,300))

####################################################################################################################

        #Create vertical slider for PackTemp
        PackTemp = wx.Slider(MainPanel, value=375, minValue=100, maxValue=500, pos=(800, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        PackTemp.Bind(wx.EVT_SCROLL, self.OnSliderScrollPT)

        #create lables for PackTemp Slider
        self.PackTempTxt  = wx.StaticText(MainPanel, label='375', pos=(802,33))
        self.PackTempTxt2 = wx.StaticText(MainPanel, label='PackTemp', pos=(780,300))

###################################################################################################################
        
        #create vertical slider for PackSOC
        PackSOC = wx.Slider(MainPanel, value=375, minValue=100, maxValue=500, pos=(950, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        PackSOC.Bind(wx.EVT_SCROLL, self.OnSliderScrollPS)

        #create lables for PackTemp Slider
        self.PackSOCTxt  = wx.StaticText(MainPanel, label='375', pos=(952,33))
        self.PackSOCTxt2 = wx.StaticText(MainPanel, label='PackSOC', pos=(930,300))

#####################################################################################################################

        #create vertical slider for PackBalance
        PackBalance = wx.Slider(MainPanel, value=375, minValue=100, maxValue=500, pos=(1100, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        PackBalance.Bind(wx.EVT_SCROLL, self.OnSliderScrollPB)

        #create lables for PackBalance Slider
        self.PackBalanceTxt  = wx.StaticText(MainPanel, label='375', pos=(1102,33))
        self.PackBalanceTxt2 = wx.StaticText(MainPanel, label='PackBalance', pos=(1080,300))

##########################################____BUTTON CREATION_____#####################################################

        
        #create toggle button for PrechargeCont
        PrechargeCont = wx.ToggleButton(MainPanel, label='PrechargeCont', pos=(30,500), size=(100,200))
        PrechargeCont.Bind(wx.EVT_TOGGLEBUTTON, self.TogglePC)

        #create toggle button for MainCont
        MainCont = wx.ToggleButton(MainPanel, label='MainCont', pos=(230,500), size=(100,200))
        MainCont.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleMC)

        #create toggle button for EStop
        EStop = wx.ToggleButton(MainPanel, label='EStop', pos=(430,500), size=(100,200))
        EStop.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleES)

        #create termination button
        TButton = wx.Button(MainPanel, label='Terminate', pos(630,500), size=(100,200))
        TButton.Bind(wx.EVT_BUTTON, self.Term)

        
        ####init the frame####
        self.Maximize()
        self.SetTitle('wx.Slider')
        self.Centre()
        self.Show(True) 

#####################################____Method Creation____#############################
    def OnSliderScrollBV(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        BusVoltageValue = obj.GetValue()
        self.BusVoltageTxt.SetLabel(str(val))
    
    def OnSliderScrollPA(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        PhaseAtempValue = obj.GetValue()
        self.PhaseAtempTxt.SetLabel(str(val))
        
    def OnSliderScrollMI(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        MotorIdValue = obj.GetValue()
        self.MotorIdTxt.SetLabel(str(val))

    def OnSliderScrollMT(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        MotorTempValue = obj.GetValue()
        self.MotorTempTxt.SetLabel(str(val))

    def OnSliderScrollMV(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        MotorVelocityValue = obj.GetValue()
        self.MotorVelocityTxt.SetLabel(str(val))

    def OnSliderScrollPT(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        PackTempValue = obj.GetValue()
        self.PackTempTxt.SetLabel(str(val))

    def OnSliderScrollPS(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        PackSOCValue = obj.GetValue()
        self.PackSOCTxt.SetLabel(str(val))

    def OnSliderScrollPB(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        PackBalanceValue = obj.GetValue()
        self.PackBalanceTxt.SetLabel(str(val))

    def TogglePC(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            PrechargeContValue = 1
        else:
            PrechargeContValue = 0

    def ToggleMC(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            MainContValue = 1
        else:
            MainContValue = 0

    def ToggleES(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            EStopValue = 1
        else:
            EStopValue = 0

    def Term(self, e):
        END = 1;
        


    
ex = wx.App(False)
windows = MainFrame(None, 'CANSim')
ex.MainLoop()



##########################_____WRITE TO DATABASE____########################

#Define tic-tok function
def tic():
    #Homemade version of matlab tic and toc functions
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    if 'startTime_for_tictoc' in globals():
        return(time.time() - startTime_for_tictoc)



#establish connection with database
con = mdb.connect('localhost','root','buckeyes','westest')


While END = 0:
        
