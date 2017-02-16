#include <stdio.h>
#include <iostream>
#include <windows.h>
#include <QString>

/* http://stackoverflow.com/questions/3331682/change-wallpaper-programmatically-using-c-and-windows-api */

int main(){
  printf("Installing Gentoo in da club");
  QString filepath = 'C:\Users\SpaceVM\Pictures\InstallingGentooInDaClub.jpg';
  char path = [150];
  char *WalP;
  cout << 'WalP'
  
  int result;
  result = SystemParametersInfo(SPI_SETDESKTOPWALLPAPER, 0, WalP, SPIF_UPDATEFILE);
  
  if(result){
    cout << "Wallpaper set";
  }
  
  else(){
    cout << "Wallpaper not set";
    cout << "SPI Returned" << result;
  
  userinput();
  return 0;
}
