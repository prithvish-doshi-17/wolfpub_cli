base_url = "http://localhost:8000/wolfpub/"
update_publication = base_url + "publication/<publication_id>/"
assign_editor = base_url + "publication/<publication_id>/"
view_publication = base_url + "employees/<employee_id>/publications"
add_article = base_url + "publication/<publication_id>/article/"
add_chapter = base_url + "publication/<publication_id>/chapter/"
delete_article = base_url + "publication/<publication_id>/article/<article_id>"
delete_chapter = base_url + "publication/<publication_id>/chapter/<chapter_id>"
new_book = base_url + "publication/book/"
new_periodical = base_url + "publication/periodical/"
update_chapter = base_url + "publication/<publication_id>/chapter/<chapter_id>/"
update_article = base_url + "publication/<publication_id>/chapter/<article_id>/"
get_content = base_url + "search/"
add_salary = base_url + "salaries/"
update_salary = base_url + "salaries/<transaction_id>/"
update_distributor = base_url + "distributors/<distributor_id>/"
get_distributor = base_url + "distributors/<distributor_id>/"
new_order = base_url + "accounts/<account_id>/orders"
new_bill = base_url + "accounts/<account_id>/bills"
monthly_report = base_url + "reports/monthly/"
distributor_count = base_url + "reports/distributors/active/count/"
get_revenue = base_url + "reports/revenue/"
salary_payments = base_url + "reports/salary-payment/"