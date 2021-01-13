import os;


class Date:
    __Year = -1;
    __Month = -1;
    __Day = -1;
    __Hour = -1;
    __Minute = -1;

    def __init__(self):

        self.__Year = -1;
        self.__Month = -1;
        self.__Day = -1;
        self.__Hour = -1;
        self.__Minute = -1;

    def GetYear(self, Year):
        self.__Year = Year;

    def GetMonth(self, Month):
        self.__Month = Month;

    def GetDay(self, Day):
        self.__Day = Day;

    def GetHour(self, Hour):
        self.__Hour = Hour;

    def GetMinute(self, Minute):
        self.__Minute = Minute;

    def __Check(self):
        return self.__Year >= 0 and self.__Month >= 0 and self.__Day >= 0 and self.__Hour >= 0 and self.__Minute >= 0;

    def Dump(self):
        if self.__Check():

            if os.path.isfile("dates/" + str(self.__Year) + str(self.__Month) + str(self.__Day) + ".csv"):
                File = open("dates/" + str(self.__Year) + str(self.__Month) + str(self.__Day) + ".csv", "a");
                File.write(str(self.__Year) + "," + str(self.__Month) + "," + str(self.__Day) + "," + str(
                    self.__Hour) + "," + str(self.__Minute) + "\n");
                File.close();
            else:
                File = open("dates/" + str(self.__Year) + str(self.__Month) + str(self.__Day) + ".csv", "w");
                File.write("Year,Month,Day,Hour,Minute\n" + str(self.__Year) + "," + str(self.__Month) + "," + str(
                    self.__Day) + "," + str(self.__Hour) + "," + str(self.__Minute) + "\n");
                File.close();

            return True;

        else:
            return False;  # Error: Campos incompletos.

    def LoadToday(self, Year, Month, Day):

        Dates = [];

        if os.path.isfile("dates/" + str(Year) + str(Month) + str(Day) + ".csv"):

            File = open("dates/" + str(Year) + str(Month) + str(Day) + ".csv", "r");

            for Line in File:
                Dates.append(Line);

            File.close();

            return Dates;

        else:

            return [];