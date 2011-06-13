echo "Digite a modificacao realizada"
#motivo=`zenity --entry --title "Commit" --text "Digite a modificacao realizada" --hide-text`
read motivo
git add cuponclipper001/
git commit -m $motivo
git push origin master
