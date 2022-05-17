HEADERS = {
    "Origin": "www.udemy.com",
    # "User-Agent":
    # "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Accept": "*/*",
    "Accept-Encoding": None,
}

SUBSCRIBED_COURSES_URL =  "https://www.udemy.com/api-2.0/users/me/subscribed-courses/?ordering=-last_accessed&fields[course]=@min,visible_instructors,image_240x135,favorite_time,archive_time,completion_ratio,last_accessed_time,enrollment_time,is_practice_test_course,features,num_collections,published_title,is_private,is_published,buyable_object_type&fields[user]=@min,job_title&page={page}&page_size={page_size}&is_archived={include_archived}"