function showTables() {
    document.getElementById("pr_table").style.display = "block";
}

function showStaff() {
    document.getElementById("staffSection").style.display = "block";
}

function getCovidInfo(){
    fetch("https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/actions/GBR/2021-05-9")
        .then((res) => res.json())
        .then((json) => {
            var numOfDeath = json["stringencyData"]["deaths"];
            var numOfCases = json["stringencyData"]["confirmed"];
            document.getElementById("covidCases").innerHTML = numOfCases;
            document.getElementById("deathCases").innerHTML = numOfDeath;
            console.log("total number of cases:" + numOfCases);
            console.log("total number of death:" + numOfDeath);
        });
    document.getElementById("covidInfo").style.display = "block";

}

//function loadInfo() {
//    var xhttp = new XMLHttpRequest();
//    xhttp.onreadystatechange = function () {
//        if (this.readyState == 4 && this.status == 200) {
//            document.getElementById("desc").innerHTML =
//                this.responseText;
//        }
//    };
    
//    xhttp.open("GET", 'ajaxinfo.txt' , true);
//    xhttp.send();
//}