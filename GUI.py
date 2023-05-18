import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do") #Ovo je ono sto ce pisati pre samo boxa za unos teksta
input_box = sg.Input(tooltip="Enter To-Do") #Ovo je ono sto bude napisano pored kursora pre nego sto se klikne
add_button = sg.Button("Add")   #Kreiranje dugmeta



window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])  #NAZIV APLIKACIJE (ono sto pise na naslovnoj traci!)
                                        #Ovo iznad ide u 2 2 uglaste jer zelimo da bude sve u jednom redu.
                                        #Da zelimo da box za unos texta bude ispod, LABEL i BOX cemo staviti u odvojene uglaste.
window.read()
print("Hello")
window.close()









