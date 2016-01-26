//-----------------------------Supporting Functions-----------------

function getDate() {
    var date = new Date();

    return date;
}

function getDifferenceInDays(date1, date2) {
    var difference = date1 - date2;

    difference = difference/86400000;
    difference = difference.toString().split(".");

    return difference[0];
}
//---------------------------------Classes----------------------------

function Summary(zone, pressure, temperature, AHU, room) {
    var self = this;
    self.zone = zone;
    self.pressure = pressure;
    self.temperature = temperature;
    self.AHU = AHU;
    self.room = room;
}

function MaintenanceCheck(target, year, month, day) {
    var self = this;
    var today = getDate();
    var date = new Date(year, month, day);
    var timeLeft = getDifferenceInDays(date, today);

    self.target = target;
    self.date = month + "-" + day + "-" + year;
    self.days = timeLeft;
    self.updateDays = function() {
        timeLeft = getDifferenceInDays(date, getDate());
        self.days(timeLeft);
    };

    setInterval(self.updateDays, 3600000);    
}

//---------------------------------Model------------------------------
function IndexViewModel() {
    var self = this;

    self.summaries = ko.observableArray([
        new Summary("a", "b", "c", "d", "e"),
        new Summary("a", "b", "c", "d", "e")
    ]);

    self.maintenanceChecks = ko.observableArray([
        new MaintenanceCheck("fire extinguisher", 2014, 8, 19)
    ]);

}

// Activates knockout.js
ko.applyBindings(new IndexViewModel(), document.getElementById('main_content'));

