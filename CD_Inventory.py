#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# nickculbert, 2021-Mar-16, added code to handle tracks
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects, lstOfTracks = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, '
              'all unsaved data will be lost '
              'and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. '
                         'Otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects, lstOfTracks = IO.FileIO.load_inventory(lstFileNames)
        else:
            input('canceling... Inventory data NOT reloaded. '
                  'Press [ENTER] to continue to the menu.')
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        try:
            cd_idx = int(input('Select the CD / Album index: '))
        except Exception:
            raise Exception('ID needs to be Integer!')            
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while True:
            IO.ScreenIO.print_CD_menu()
            subMenuChoice = IO.ScreenIO.menu_CD_choice()
            if subMenuChoice == 'x':
                break
            elif subMenuChoice == 'a':
                newTrack = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(newTrack, cd)
                continue
            elif subMenuChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
                continue
            elif subMenuChoice == 'r':
                try:
                    track_id = int(input('Enter the track number: '))
                except Exception:
                    raise Exception('ID needs to be Integer!')                    
                PC.CD.rmv_track(track_id)
                continue
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects, lstOfTracks)
        else:
            input('The inventory was NOT saved to file. '
                  'Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')