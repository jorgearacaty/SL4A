echo --------------------------------------------------
echo refresh GitHub a cada ciclo de atualização.
echo jorgearacaty, 5 aug 2014 - 2151.
echo --------------------------------------------------

:: 'cd C:\\\Users\\CCE\\Desktop\\GetGit\\excel_help'

git add @.bat
git add @pull.bat
git add @set_remote.bat
git add calcula_estatistica_de_um_intervalo.xlsm
git add excel_help.xlsm
git add leiaME.docx
git add MEleia.txt 
git add mosaico.xlms.txt
git add mosaico.xlsm
git add README.md

git commit -m "jorgearacaty" 
git push -u origin master 