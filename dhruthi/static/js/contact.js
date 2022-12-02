
let bookingform = document.querySelector('.book-apponintment');

// let select_value  = document.querySelector('#branch_item');
// let submit_btn = document.querySelector('#submit');
let inputs = document.querySelectorAll('input')
let textariea = document.querySelector('textarea')
bookingform.addEventListener('submit', function(event){
          event.preventDefault();
          $.ajax({
            type:'POST',
            url:'/',
            data:{
              name:$("#name").val(),
              email:$("#email").val(),
              phone:$("#phone").val(),
              date:$("#date").val(),
              branch:$('#branch_item').find(":selected").val(),
              message:$("#message").val(),
              csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data) {
         
              swal("success", "Your Message was sending successfully ", "success");
            
            },
            error: function(xhr, status, error) {
              swal("error!", "Please Try Agian", "error");
            
            },
            dataType: 'text'
        })
        inputs.forEach(input => input.value = '');
        textariea.value =''
}) 