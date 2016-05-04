from gi.repository import Gtk
import work_space as ws
import analyza as na
import numpy as np


class UserInterface(Gtk.Window):
    def __init__(self):
        print("start init")
        Gtk.Window.__init__(self, title="LEA")
        self.sizes=64
        self.fileNames='keyMatrix/SmallKey.txt'
        self.file2De=" "
        self.set_size_request(800, 600)
        table = Gtk.Table(10, 6, True)
        self.add(table) 
        def files():
            #KEY MATRIX
            na.createEncryptMatrix(self.sizes, self.sizes,self.fileNames)
            
        def Buttons():
            # Buttons of GUI
            #browsers
            self.browse1 = Gtk.Button(label="Browse image file")
            self.browse1.connect("clicked", self.on_open_clicked1, self.sizes, self.sizes)
            self.browse2 = Gtk.Button(label="Browse txt file")
            self.browse2.connect("clicked", self.on_open_clicked2, self.sizes, self.sizes)
            self.encrypt = Gtk.Button(label="Encrypt")
            self.encrypt.connect("clicked", self.encrypt_image_prog)
            self.decrypt = Gtk.Button(label="Decrypt")
            self.decrypt.connect("clicked", self.decrypt_image_prog)
            self.exit = Gtk.Button(label="Exit")
            self.exit.connect("clicked", self.destroy_exit_prog)
            self.help = Gtk.Button(label="Help")
            self.help.connect("clicked",self.on_help_clicked)
            table.attach(self.browse1, 1,2,3,4)  
            table.attach(self.browse2, 1,2,4,5)
            table.attach(self.encrypt, 3, 5, 8, 9)
            table.attach(self.decrypt, 3, 5, 9, 10)
            table.attach(self.help, 1, 2, 8, 9)
            table.attach(self.exit, 1, 2, 9, 10)
        def Labels():
            # Labels of GUI
            Label_Dec = Gtk.Label("Decrypted")
            Label_Enc = Gtk.Label("Encrypted") 
            Label_Or = Gtk.Label("Original") 
            table.attach(Label_Dec, 0, 2, 0, 1)
            table.attach(Label_Enc, 2, 4, 0, 1)
            table.attach(Label_Or, 4, 6, 0, 1)
        def Images():
            # Images of GUI
            self.image = Gtk.Image.new_from_icon_name("process-stop", Gtk.IconSize.MENU)        
            self.image1 = Gtk.Image.new_from_icon_name("process-stop", Gtk.IconSize.MENU)
            self.image2 = Gtk.Image.new_from_icon_name("process-stop", Gtk.IconSize.MENU)    
            table.attach(self.image, 0, 2, 1, 3)
            table.attach(self.image1, 2, 4, 1, 3)
            table.attach(self.image2, 4, 6, 1, 3)
        Buttons()
        Labels()
        Images()
        files()
        print(" init")      
    def destroy_exit_prog(self, widget, data=None):
        Gtk.main_quit() 
    def on_help_clicked(self, widget):
        #************************************************************************
        #To do
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "Program HELP")
        dialog.format_secondary_text(
            "                                                         MENU       \n\n\n\n"+                         
            "1: Run start_gui.py\n"+
            "2: Press on Browse image file button and choose image.\n"+
            "3: You will see in right image screen the Original image.\n"+
            "4: Press on Encrypt button.\n"+
            "5: You will see the Encrypted image.\n"+
            "6: Press on browse txt file and choose Encrypted.txt file from data folder.\n"+
            "7: Press on Decrypt it's take few seconds and you will see Decrypted image\n")
        dialog.run()

        dialog.destroy()
        #************************************************************************      
    def on_open_clicked1 (self, widget, *data):
        self.choise=0
        dialog = Gtk.FileChooserDialog ("Open Image", widget.get_toplevel(), Gtk.FileChooserAction.OPEN);
        dialog.add_button(Gtk.STOCK_CANCEL, 0)
        dialog.add_button(Gtk.STOCK_OK, 1)
        dialog.set_default_response(1)

        filefilter = Gtk.FileFilter ()
        filefilter.add_pixbuf_formats ()
        dialog.set_filter(filefilter)

        if dialog.run() == 1:
            ws.change_resolution(dialog.get_filename(), data[0], data[1]) #chane resolution
            pathImage=dialog.get_filename()
            ws.image_show(pathImage) #show image
            imageFile = "images/SHOW.jpg"
            self.image2.set_from_file(imageFile)
        dialog.destroy()               
    
    def on_open_clicked2 (self, widget, *data):
        self.choise=0
        dialog = Gtk.FileChooserDialog ("Open txt file", widget.get_toplevel(), Gtk.FileChooserAction.OPEN);
        dialog.add_button(Gtk.STOCK_CANCEL, 0)
        dialog.add_button(Gtk.STOCK_OK, 1)
        dialog.set_default_response(1)

        filefilter = Gtk.FileFilter ()
        filefilter.add_pattern('*.txt')
        dialog.set_filter(filefilter)
        if dialog.run() == 1:
            self.file2De=dialog.get_filename()
        print(self.file2De)
        
            
        dialog.destroy()    
    def encrypt_image_prog(self,*data):
        #check date:16.03.2016
        if(self.choise==-1):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "Program HELP")
            dialog.format_secondary_text("you must choose image before Encrypt/Decrypt")
            dialog.run()
            dialog.destroy()
            return
        
        # Global parameter var. have resolution of image if you need it to create special matrix "2048 or 1024 or 800: :)))) 
        image = "images/ANTIALIAS.jpg"
        matImage = ws.image_to_matrix(image)
        key_mat= na.file_to_matrix(self.fileNames)
        sizeM=self.sizes
        na.matrix_to_file('data/Original.txt', matImage, sizeM, sizeM)
        # here must be inquiries to encryption functions 
        #ONLY 4 LARGE  
        
        na.encrypt(np.array(key_mat), sizeM,sizeM,matImage, sizeM,sizeM)
        mat_list=na.file_to_matrix('data/EncryptedNormal.txt')
        #enc_mat =array.array('l',mat_list)
        mat_list=np.array( mat_list,np.uint8)
        ws.matrix_to_image( mat_list) # change to <enc_mat> , matImage only for check
        ws.image_show("images/output.jpg")  
        imageFile = "images/SHOW.jpg"
        self.image1.set_from_file(imageFile)
        
        
    def decrypt_image_prog(self,*data):
        if(self.choise==-1 or self.file2De==" "):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "Program HELP")
            dialog.format_secondary_text("you must choose image before Encrypt/Decrypt")
            dialog.run()
            dialog.destroy()
            return
        
        matFile=na.file_to_matrix(self.file2De)
        #image = "images/ANTIALIAS.jpg"
        #matImage = ws.image_to_matrix(image)
        # here must be inquiries to decryption functions
        #ONLY 4 LARGE
        key_mat= na.file_to_matrix(self.fileNames)
        sizeM=self.sizes
        na.decrypt(np.array(key_mat), sizeM,sizeM,matFile, sizeM,sizeM)
        
        dec_mat=na.file_to_matrix('data/DecryptedNormal.txt')
        
        #enc_mat =array.array('l',mat_list)
        dec_mat=np.array( dec_mat,np.uint8)
        
        ws.matrix_to_image(dec_mat)
        ws.image_show("images/output.jpg")
        imageFile = "images/SHOW.jpg"
        self.image.set_from_file(imageFile)
        
win = UserInterface()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()