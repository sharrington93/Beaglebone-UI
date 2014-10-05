import wx
import MySQLdb as mdb
import sys
import time
import thread
from wx.lib.pubsub import setuparg1
from wx.lib.pubsub import pub


###init global variables###
PhaseAtempValue = 50
BusVoltageValue = 375
MotorIdValue = 150
MotorTempValue = 50
MotorVelocityValue = 1500
PackTempValue = 25
PackSOCValue = 50
PackBalanceValue = 80
PrechargeContValue = 0
MainContValue = 0
EStopValue = 0
Pause = 0
i=0


def serverContact():
    #establish connection with database
    con = mdb.connect('192.168.7.35','dbUser','buckeyes','westest')
    print('TEST')

    with con:
        #establish pointer
        cur = con.cursor()
        
        #Drop table Names if it exists
        cur.execute("DROP TABLE IF EXISTS Names")

        #creates table of Names
        cur.execute("CREATE TABLE Names(MsgName TEXT, Unit TEXT, OkMin FLOAT, OkMax FLOAT, WarnMin FLOAT, WarnMax FLOAT)")

        #occupies table Names with values
        cur.executemany("""INSERT INTO Names(MsgName, Unit, OkMin, OkMax, WarnMin, WarnMax)
                    VALUES (%s,%s,%s,%s,%s,%s)""",
                        [
                        ('PhaseAtemp','C','5','60','0','90'),
                        ('BusVoltage','V','350','450','250','470'),
                        ('MotorId','A','0','250','0','280'),
                        ('MotorTemp','C','5','90','0','110'),
                        ('MotorVelocity','RPM','0','2500','0','3000'),
                        ('PackTemp','C','0','50','0','75'),
                        ('PackSOC','%','25','100','5','100'),
                        ('PackBalance','%','75','100','60','100')
                        ])
        con.commit()
        
        cur.executemany("""INSERT INTO Names(MsgName) VALUES (%s)""",
                        [
                        ('PrechargeCont'),
                        ('MainCont'),
                        ('EStop')
                        ])
        con.commit()

        
        #Drop table Messages if it exists
        cur.execute("DROP TABLE IF EXISTS Messages")

        #creates table to be occupied with date
        cur.execute("CREATE TABLE Messages(time BIGINT, MsgName TEXT, Value FLOAT, INDEX(time))")
        
        

        global i
        for i in range(0,1800):
            wx.CallAfter(pub.sendMessage,'changei',i)
            #import pdb; pdb.set_trace()
            time.sleep(.5)
            cur.executemany('''INSERT INTO Messages(time, MsgName, Value)
                        VALUES(%s,%s,%s)''',
                [
                (str(time.time()*1000),'PhaseAtemp',str(PhaseAtempValue)),
                (str(time.time()*1000),'BusVoltage',str(BusVoltageValue)),
                (str(time.time()*1000),'MotorId',str(MotorIdValue)),
                (str(time.time()*1000),'MotorTemp',str(MotorTempValue)),
                (str(time.time()*1000),'MotorVelocity',str(MotorVelocityValue)),
                (str(time.time()*1000),'PackTemp',str(PackTempValue)),
                (str(time.time()*1000),'PackSOC',str(PackSOCValue)),
                (str(time.time()*1000),'PackBalance',str(PackBalanceValue)),
                (str(time.time()*1000),'PrechargeCont',str(PrechargeContValue)),
                (str(time.time()*1000),'MainCont',str(MainContValue)),
                (str(time.time()*1000),'EStop',str(EStopValue))
                ]) 
            con.commit()
            while Pause == 1:
                time.sleep(.1)

########################################################################################
def dispGUI():
    ex = wx.App(False)
    windows = MainFrame(None, 'CANSim')
    ex.MainLoop()


##########################################################################
class MainFrame(wx.Frame):
           
    def __init__(self, parent, id):
        wx.Frame.__init__(self, None, title = 'CANSim')
        
        self.InitUI()

    def changeDisp(self, message):
        self.cycles.SetLabel(str(message.data))

    def InitUI(self):
        pub.subscribe(self.changeDisp, ('changei'))
        MainPanel = wx.Panel(self)

        #display cycles
        self.cycles = wx.StaticText(MainPanel, label=str(i), pos=(830,500))

        #Create Vertical Slider for BusVoltage
        BusVoltage = wx.Slider(MainPanel, value=375, minValue=150, maxValue=550, pos=(50, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        BusVoltage.Bind(wx.EVT_SCROLL, self.OnSliderScrollBV)

        #create labels for BusVoltage Slider
        self.BusVoltageTxt  = wx.StaticText(MainPanel, label='375', pos=(52, 33))
        self.BusVoltageTxt2 = wx.StaticText(MainPanel, label='BusVoltage',pos=(30,300))


######################################################################################################################
        
        #Create Vertical Slider for PhaseAtemp
        PhaseAtemp = wx.Slider(MainPanel, value=50, minValue=0, maxValue=120, pos=(200, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        PhaseAtemp.Bind(wx.EVT_SCROLL, self.OnSliderScrollPA)

        #create labels for PhaseAtemp Slider
        self.PhaseAtempTxt  = wx.StaticText(MainPanel, label='50', pos=(202, 33))
        self.PhaseAtempTxt2 = wx.StaticText(MainPanel, label='PhaseAtemp',pos=(180,300))
        
######################################################################################################################      

        #Create Vertical Slider for MotorId
        MotorId = wx.Slider(MainPanel, value=150, minValue=0, maxValue=300, pos=(350, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        MotorId.Bind(wx.EVT_SCROLL, self.OnSliderScrollMI)
        
        #create lables for MotorId Slider
        self.MotorIdTxt  = wx.StaticText(MainPanel, label='150', pos=(352,33))
        self.MotorIdTxt2 = wx.StaticText(MainPanel, label='MotorId', pos=(330,300))

######################################################################################################################

        #Create vertical slider for MotorTemp
        MotorTemp = wx.Slider(MainPanel, value=50, minValue=0, maxValue=130, pos=(500, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        MotorTemp.Bind(wx.EVT_SCROLL, self.OnSliderScrollMT)

        #create lables for MotorTemp Slider
        self.MotorTempTxt  = wx.StaticText(MainPanel, label='50', pos=(502,33))
        self.MotorTempTxt2 = wx.StaticText(MainPanel, label='MotorTemp', pos=(480,300))

#####################################################################################################################

        #Create vertical slider for MotorVelocity
        MotorVelocity = wx.Slider(MainPanel, value=1500, minValue=0, maxValue=3500, pos=(650, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        MotorVelocity.Bind(wx.EVT_SCROLL, self.OnSliderScrollMV)

        #create lables for MotorVelocity Slider
        self.MotorVelocityTxt  = wx.StaticText(MainPanel, label='1500', pos=(652,33))
        self.MotorVelocityTxt2 = wx.StaticText(MainPanel, label='MotorVelocity', pos=(630,300))

####################################################################################################################

        #Create vertical slider for PackTemp
        PackTemp = wx.Slider(MainPanel, value=25, minValue=0, maxValue=100, pos=(800, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        PackTemp.Bind(wx.EVT_SCROLL, self.OnSliderScrollPT)

        #create lables for PackTemp Slider
        self.PackTempTxt  = wx.StaticText(MainPanel, label='25', pos=(802,33))
        self.PackTempTxt2 = wx.StaticText(MainPanel, label='PackTemp', pos=(780,300))

###################################################################################################################
        
        #create vertical slider for PackSOC
        PackSOC = wx.Slider(MainPanel, value=50, minValue=0, maxValue=100, pos=(950, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        PackSOC.Bind(wx.EVT_SCROLL, self.OnSliderScrollPS)

        #create lables for PackTemp Slider
        self.PackSOCTxt  = wx.StaticText(MainPanel, label='50', pos=(952,33))
        self.PackSOCTxt2 = wx.StaticText(MainPanel, label='PackSOC', pos=(930,300))

#####################################################################################################################

        #create vertical slider for PackBalance
        PackBalance = wx.Slider(MainPanel, value=80, minValue=0, maxValue=100, pos=(1100, 50), size=(-1, 250), style=wx.SL_VERTICAL)
        PackBalance.Bind(wx.EVT_SCROLL, self.OnSliderScrollPB)

        #create lables for PackBalance Slider
        self.PackBalanceTxt  = wx.StaticText(MainPanel, label='80', pos=(1102,33))
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


        #create pause toggle button
        PButton = wx.ToggleButton(MainPanel, label='Pause',pos=(630,500),size=(100,200))
        PButton.Bind(wx.EVT_TOGGLEBUTTON, self.Pause)

        
        ####init the frame####
        self.Maximize()
        self.SetTitle('wx.Slider')
        self.Centre()
        self.Show(True)

       

#####################################____Method Creation____#############################
    def OnSliderScrollBV(self, e):
        global BusVoltageValue
        obj = e.GetEventObject()
        val = obj.GetValue()
        BusVoltageValue = obj.GetValue()
        self.BusVoltageTxt.SetLabel(str(val))
    
    def OnSliderScrollPA(self, e):
        global PhaseAtempValue
        obj = e.GetEventObject()
        val = obj.GetValue()
        PhaseAtempValue = obj.GetValue()
        self.PhaseAtempTxt.SetLabel(str(val))
        
    def OnSliderScrollMI(self, e):
        global MotorIdValue
        obj = e.GetEventObject()
        val = obj.GetValue()
        MotorIdValue = obj.GetValue()
        self.MotorIdTxt.SetLabel(str(val))

    def OnSliderScrollMT(self, e):
        global MotorTempValue
        obj = e.GetEventObject()
        val = obj.GetValue()
        MotorTempValue = obj.GetValue()
        self.MotorTempTxt.SetLabel(str(val))

    def OnSliderScrollMV(self, e):
        global MotorVelocityValue
        obj = e.GetEventObject()
        val = obj.GetValue()
        MotorVelocityValue = obj.GetValue()
        self.MotorVelocityTxt.SetLabel(str(val))

    def OnSliderScrollPT(self, e):
        global PackTempValue
        obj = e.GetEventObject()
        val = obj.GetValue()
        PackTempValue = obj.GetValue()
        self.PackTempTxt.SetLabel(str(val))

    def OnSliderScrollPS(self, e):
        global PackSOCValue
        obj = e.GetEventObject()
        val = obj.GetValue()
        PackSOCValue = obj.GetValue()
        self.PackSOCTxt.SetLabel(str(val))

    def OnSliderScrollPB(self, e):
        global PackBalanceValue
        obj = e.GetEventObject()
        val = obj.GetValue()
        PackBalanceValue = obj.GetValue()
        self.PackBalanceTxt.SetLabel(str(val))

    def TogglePC(self, e):
        global PrechargeContValue
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            PrechargeContValue = 1
        else:
            PrechargeContValue = 0

    def ToggleMC(self, e):
        global MainContValue
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            MainContValue = 1
        else:
            MainContValue = 0

    def ToggleES(self, e):
        global EStopValue
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            EStopValue = 1
        else:
            EStopValue = 0


    def Pause(self, e):
        global Pause
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            Pause = 1
        else:
            Pause = 0
            



########################################################################
thread.start_new_thread(dispGUI,())
thread.start_new_thread(serverContact,())





