$(document).ready(function () {
    $("#myTable").DataTable();
    $("#approveAll").on("click", function () {
      $('input[value="approve"]').prop("checked", true);
    });
    $("#denyAll").on("click", function () {
      $('input[value="reject"]').prop("checked", true);
    });
     $('input[type="radio"]').on("click", updateCount);
  });
  
  function updateCount(){
    var total = $('table input[value="approve"]').length;
    var countApprove = $('table input[value="approve"]:checked').length;
    var countDeny = $('table input[value="reject"]:checked').length; 
    $('#changesCount').text((countApprove + countDeny) + ' changes ');
    console.log(total, countApprove, countDeny);
    
    if(total === countApprove){
      $('#approveAll').prop("checked", true);
      return;
    }
    if(total === countDeny){
      $('#denyAll').prop("checked", true);
      return;
    }
    $('#denyAll,#approveAll').prop("checked", false);
  }