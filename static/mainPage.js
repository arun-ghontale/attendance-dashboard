
//let studentAttendance = {
//  "Java": {
//    "Students": [{
//      "Student": "Cristiano Ronaldo",
//      "Classes Attended": 4
//    }, {
//      "Student": "Bruno Fernandes",
//      "Classes Attended": 3
//    },{
//      "Student": "Mason Greenwood",
//      "Classes Attended": 3
//    }, {
//      "Student": "Rafael Varane",
//      "Classes Attended": 3
//    }],
//    "Total Classes": 5
//  },
//  "Python": {
//    "Students": [{
//      "Student": "Jadon Sancho",
//      "Classes Attended": 4
//    }, {
//      "Student": "Cristiano Ronaldo",
//      "Classes Attended": 6
//    }, {
//      "Student": "Bruno Fernandes",
//      "Classes Attended": 3
//    }, {
//      "Student": "Mason Greenwood",
//      "Classes Attended": 7
//    }],
//    "Total Classes": 8
//  },
//  "Node": {
//    "Students": [{
//      "Student": "McTominay",
//      "Classes Attended": 3
//    }, {
//      "Student": "Anthony Elanga",
//      "Classes Attended": 15
//    }, {
//      "Student": "Juan Mata",
//      "Classes Attended": 18
//    }, {
//      "Student": "George Best",
//      "Classes Attended": 20
//    }],
//    "Total Classes": 20
//  }
//}
let studentAttendance;

$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        url: "/student-report-json",
        success:function(data){
              studentAttendance = JSON.parse(data);
              let classes = Object.keys(studentAttendance);
              classes.forEach((item, index)=>{
                  let htmlText = `<a class="dropdown-item" onclick="onClassSelect('${item}')" href="#">${item}</a>`
              $("#classes-dropdown").append(htmlText);
              let pickRandomClass = classes[Math.floor(Math.random() * classes.length)];
              $("#navbarDropdown").text(pickRandomClass);
              $("#attendance-list").empty();
              generateAttendanceList(pickRandomClass);

              });
        }
    });


  toastr.options = {
  "closeButton": false,
  "debug": false,
  "newestOnTop": true,
  "progressBar": false,
  "positionClass": "toast-bottom-center",
  "preventDuplicates": false,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "2000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
}
});

function generateAttendanceList(className){
  let htmlText = "";
  htmlText += `<ul class="list-group">`;
  let students = studentAttendance[className]["Students"];
  let totalClasses = studentAttendance[className]["Total Classes"];
  students.forEach((item, index)=>{
    let studentName = item["Student"];
    let attendancePercentage = 100 * item["Classes Attended"] / totalClasses;
    let classesAttended = item["Classes Attended"];
    if (attendancePercentage >= 75){
      htmlText += `\n<li class="list-group-item list-group-item-success">
    <p style="text-align:left;">
      <h4>${studentName}<span style="float:right;">${attendancePercentage}% (${classesAttended}/${totalClasses})</span></h4>
    </p>
    </li>`
    }
    else{
     htmlText += `\n<li class="list-group-item list-group-item-danger">
    <p style="text-align:left;">
      <h4>${studentName}<span style="float:right;">${attendancePercentage}% (${classesAttended}/${totalClasses})</span></h4>
    </p>
    </li>`
    }
    htmlText += `\n</ul>`;
  });
      $("#attendance-list").append(htmlText);
}

function onClassSelect(className){
  $("#navbarDropdown").text(className);
  $("#attendance-list").empty();
  generateAttendanceList(className);
}

function sendReport(){
  $('#send-report-yes').prop('disabled', true);
  $('#send-report-no').prop('disabled', true);
  $('#send-report-btn').prop('disabled', true);

  setTimeout(function(){
      $.ajax({
        type: 'GET',
        url: "/send-report",
        success:function(data){
                toastr["success"]("Report Sent Successfully", "Send Report")
                $('#send-report-yes').prop('disabled', false);
                $('#send-report-no').prop('disabled', false);
                $('#send-report-btn').prop('disabled', false);

                $('#send-report-modal').modal('hide');
        },
        error: function(xhr, textStatus, errorThrown){
                toastr["error"]("Report Couldn't Be Sent", "Send Report")
                $('#send-report-yes').prop('disabled', false);
                $('#send-report-no').prop('disabled', false);
                $('#send-report-btn').prop('disabled', false);
                $('#send-report-modal').modal('hide');
            }
        });
  }, 3000);
}