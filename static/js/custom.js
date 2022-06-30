function sendArticleComment(articleId) {
    var parent_id = $('#parent_id').val();
    var comment = $('#commentText').val();
    var full_name = $('#name').val();
    var email = $('#email').val();
    $.get('/articles/add-article-comment', {
        articleId: articleId, parent_id, comment, full_name, email,
    }).then(res => {
        if (res.status === 'PageLogin') {
            Swal.fire({
                title: 'اعلان',
                text: res.text,
                icon: res.icon,
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: res.confirmButtonText
            }).then(result => {
                if (result.isConfirmed && res.status === 'PageLogin') {
                    window.location = '/accounts/LogInAndSingIn/'
                }
            });
        } else if (res.status === 'Invalid') {
            document.getElementById('PDangerArticle').innerHTML = 'لطفاََ همه موارد دارای ستاره را درست پر کنید.'
        } else {
            $('#form_id').html(res);
            $('#parent_id').val('')
            $('#commentText').val('')
            document.getElementById('PDangerArticle').innerHTML = ''
            if (parent_id !== '' && parent_id !== null) {
                document.getElementById('single_comment_box_' + parent_id).scrollIntoView({behavior: "smooth"})
            } else {
                document.getElementById('comments_area').scrollIntoView({behavior: "smooth"})
            }
        }
    });
}

function FillParentId(commentId) {
    console.log(commentId)
    $('#parent_id').val(commentId)
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"})
}

function FilterProduct() {
    const filterPrice = $('#sl2').val();
    const start_price = filterPrice.split(',')[0]
    const end_price = filterPrice.split(',')[1]
    $('#start_price').val(start_price);
    $('#end_price').val(end_price);
    $('#filter_form').submit();
}

function ShowImageLarge(imageSrc) {
    $('#main_image').attr('src', imageSrc)
    $('#show_large_image_model').attr('href', imageSrc)
}

function fillPage(page) {
    $('#page').val(page);
    $('#filter_form').submit()
}

function sendProductComment(productId) {
    var full_name = $('#name_id').val();
    var email = $('#email_id').val();
    var text = $('#text_id').val();
    $.get('/products/add-comment-product/', {
        productId, full_name, email, text
    }).then(res => {
        if (res.status === 'Invalid') {
            document.getElementById("PDangerProduct").innerHTML = "لطفاََ همه ی موارد دارای ستاره را درست پر کنید.";
        } else if (res.status === 'PageLogin') {
            window.location = '/accounts/LogInAndSingIn'
        } else {
            document.getElementById('reviews').scrollIntoView({behavior: "smooth"})
            $('#name_id').val('')
            $('#email_id').val('')
            $('#text_id').val('')
            $('#commetns').html(res);

        }
    })
}

function BasketCount(detail_id, state) {
    $.get('/Order/change-detail-count', {
        detail_id, state
    }).then(res => {
        debugger;
        if (res.status === 'success') {
            $('#basket').html(res.body);
        }
    })
}

function AddProductToOrder(product_id) {
    var product_count = $('#ProductCount').val();
    $.get('/Order/add-product-to-order', {product_id, product_count}).then(res => {
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirmButtonText
        }).then(result => {
            console.log(result)
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location = '/accounts/LogInAndSingIn/'
            }
        });
    });
}

function DeleteDetail(detail_id) {
    $.get('/Order/delete-order-detail', {
        detail_id
    }).then(res => {
        if (res.status === 'success') {
            $('#basket').html(res.body)
        }
    })
}

function SendEmailToSendNews() {
    var email = $('#email').val()
    $.get('/add-email-to-send-news', {
        email: email
    }).then(res => {
        debugger;
        if (res.status === 'success') {
            document.getElementById('PSendEmail').innerHTML = 'ایمیل شما با موفقیت ثبت شد.'
            document.getElementById('PSendEmail').classList = 'text-success'
            $('#email').val('')
        } else if (res.status === 'Invalid') {
            document.getElementById('PSendEmail').innerHTML = 'لطفاََ یک ایمیل صحیح وارد کنید.'
            document.getElementById('PSendEmail').classList = 'text-danger'
        } else if (res.status === 'Repetitious') {
            document.getElementById('PSendEmail').innerHTML = 'ایمیل شما قبلاََ ثبت شده است.'
            document.getElementById('PSendEmail').classList = 'text-success'
            $('#email').val('')
        }
    })
}

function MyMessage() {
    Swal.fire({
        title: 'اعلان',
        text: 'این سایت برای نمونه کار نوشته شده است ممنون بابت اعتماد شما.',
        icon: 'success',
        showCancelButton: false,
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'خیلی هم عالی'
    }).then(result => {
        if (result.isConfirmed && res.status === 'PageLogin') {
            window.location = '/accounts/LogInAndSingIn/'
        }
    });
}