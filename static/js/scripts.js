$("form[name=signup_form").submit(function(e){
    var $form =$(this);
    var $error =$form.find(".error");
    var data =$form.serialize();

    e.preventDefault();

    $.ajax({
        url:"/user/signup",
        type:"POST",
        data:data,
        dataType: "json",
        success:function(resp){
            console.log(resp);
            window.location.href="/prediction";
        },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })
});

$("form[name=login_form").submit(function(e){
    var $form =$(this);
    var $error =$form.find(".error");
    var data =$form.serialize();

    e.preventDefault();

    $.ajax({
        url:"/user/login",
        type:"POST",
        data:data,
        dataType: "json",
        success:function(resp){
            // console.log(resp);
            window.location.href="/prediction";
        },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })
});