function storeusername(){
    username = document.getElementById("username").value
    localStorage.setItem('username', username)
}