# 
# ASHaltMessage.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init screen ASHaltMessage(error=""):
    tag ASHaltMessage
    zorder 500
    modal True
    
    on "show":
        action [
                Function(SetThumbnailFull),
                FileTakeScreenshot(),
                Function(SetThumbnailOriginal)
                ]

    add FileCurrentScreenshot()

    frame at ASDynamicBlurTransition:
        style "ASDynamicBlurFrame"
        xfill True
        yfill True

        vbox:
            xalign 0.5
            yalign 0.5
            xsize 676
            
            add ASHalt.bundleDir + "Resources/Elements/HaltSymbol.png":
                xalign 0.5
            
            null height 8
            
            vbox:
                spacing 10
            
                text "AliceOS needs to restart because a critical error has occured.":
                    style "ASHaltMessageTitle"
                    xalign 0.5
                text "You can search the Error Database for more information by going to https://errordb.aliceos.app or by scanning the QR code below.":
                    style "ASHaltMessageDetails"
                    xalign 0.5
            
            null height 32
            
            add ASHalt.bundleDir + "Resources/Elements/QRCode.png":
                xalign 0.5
            
            null height 16
            
            text error:
                style "ASHaltMessageCode"
                xalign 0.5

    timer 10.0 action Return()
