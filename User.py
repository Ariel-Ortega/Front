
from io import open;
import os;

class User:

    def __init__(self):
        pass;

    def __FirstTime(self, TypeOfUser):

        TypeOfUser = str(TypeOfUser);

        if TypeOfUser == "root":
            File = open("usr\\root\\root.dat", "r");
        else:
            if TypeOfUser == "admin":
                File = open("usr\\admin\\admin.dat", "r");
            else:
                if TypeOfUser == "assistant":
                    File = open("usr\\assistant\\assistant.dat", "r");
                else:
                    return 3;  # Error: Usuario no encontrado.

        Line = File.readline();
        Line = Line.split();

        if Line[0] == TypeOfUser and Line[1] == TypeOfUser:
            File.close();
            return True;
        else:
            File.close();
            return False;

    def CreateUser(self,Name,Password,TypeOfUser):

        Name = str(Name);
        Password = str(Password);
        TypeOfUser = str(TypeOfUser);

        IsFirstTime = self.__FirstTime(TypeOfUser);

        if IsFirstTime == True:

            if TypeOfUser == "root":

                File = open("usr\\root\\root.dat", "w");
                File.write("fhbshzwxecrvtbvecwxdszddfghgzadsfdgcfb asdjnlakyutkhujtuknybjnjyukylmunikiynimuibtjdb");
                File.close();
                self.CreateUser(self, Name, Password, TypeOfUser);

            else:
                if TypeOfUser == "admin":

                    File = open("usr\\admin\\admin.dat", "w");
                    File.write("fhbshgsdgeargerqgererwgerwgwregwrgerwgerwgrefb asdjnlafvabgxnhdcbgsbgvkjdb");
                    File.close();
                    self.CreateUser(self, Name, Password, TypeOfUser);

                else:
                    if TypeOfUser == "assistant":

                        File = open("usr\\assistant\\assistant.dat", "w");
                        File.write("fasfeffqwefweferferferrgaerghbshfb asdvxatbwdeyuqegfywqcgfoywmerjnlakjdb");
                        File.close();
                        self.CreateUser(self, Name, Password, TypeOfUser);

        else:
            if TypeOfUser == "assistant":
                File = open("usr\\assistant\\" + Name + "assistant.bin","wb");
                File.write(str(Name + " " + Password + "\n"));
                File.close();

            else:
                if TypeOfUser == "root":
                    File = open("usr\\root\\" + Name + "root.bin","wb");
                    File.write(str(Name + " " + Password + "\n"));
                    File.close();
                else:
                    if TypeOfUser == "admin":
                        File = open("usr\\admin\\" + Name + "admin.bin","wb");
                        File.write(str(Name + " " + Password + "\n"));
                        File.close();


    def SetNewPassword(self, Name, OldPassword, NewPassword,TypeOfUser):

        Name = str(Name);
        OldPassword = str(OldPassword);
        NewPassword = str(NewPassword);
        TypeOfUser = str(TypeOfUser);

        if TypeOfUser == "assistant":

            try:

                File = open("usr\\assistant\\" + Name + "assistant.bin", "rb");
                Line = File.readline().split();

                if Line[0] == Name and Line[1] == OldPassword:
                    File.close()
                    File = open("usr\\assistant\\" + Name + "assistant.bin", "wb");
                    File.write(str(Name + " " + NewPassword + "\n"));

                File.close();

            except:

                File.close();
                return "Error: No existe el usuario:";


        else:

            if TypeOfUser == "root":

                try:

                    File = open("usr\\root\\" + Name + "root.bin", "rb");

                    Line = File.readline().split();

                    if Line[0] == Name and Line[1] == OldPassword:
                        File.close();
                        File = open("usr\\root\\" + Name + "root.bin", "wb");
                        File.write(str(Name + " " + NewPassword + "\n"));

                    File.close();

                except:

                    File.close();
                    return "Error: No existe el usuario.";

            else:
                try:

                    if TypeOfUser == "admin":
                        File = open("usr\\admin\\" + Name + "admin.bin", "wb");
                        Line = File.readline().split();

                        if Line[0] == Name and Line[1] == OldPassword:
                            File.close();
                            File = open("usr\\admin\\" + Name + "admin.bin", "wb");
                            File.write(str(Name + " " + NewPassword + "\n"));

                        File.close();

                except:

                    File.close();
                    return "Error: No existe el usuario.";


    def ValidUser(self, Name, Password, TypeOfUser):

        Name = str(Name);
        Password = str(Password);
        TypeOfUser = str(TypeOfUser);

        if TypeOfUser == "root":
            if os.path.isfile("usr\\root\\" + Name + "root.bin"):
                File = open("usr\\root\\" + Name + "root.bin","rb");
                Line = File.readline().split();

                if Line[0] == Name and Line[1] == Password:
                    return True;
                else:
                    return False;

            else:
                return False;

        else:
            if TypeOfUser == "admin":
                if os.path.isfile("usr\\admin\\" + Name + "admin.bin"):
                    File = open("usr\\admin\\" + Name + "admin.bin", "rb");
                    Line = File.readline().split();

                    if Line[0] == Name and Line[1] == Password:
                        return True;
                    else:
                        return False;

                else:
                    return False;

            else:
                if TypeOfUser == "assistant":
                    if os.path.isfile("usr\\assistant\\" + Name + "assistant.bin"):
                        File = open("usr\\assistant\\" + Name + "assistant.bin", "rb");
                        Line = File.readline().split();

                        if Line[0] == Name and Line[1] == Password:
                            return True;
                        else:
                            return False;

                    else:
                        return False;

                else:

                    return False;
