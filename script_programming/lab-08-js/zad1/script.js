function write(){
    console.log(document.forms[0].elements[0].value)
    console.log(typeof document.forms[0].elements[0].value)
    console.log(document.forms[0].elements[1].value)
    console.log(typeof document.forms[0].elements[1].value)
}
document.forms[0].elements[2].onclick = write