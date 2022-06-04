HEADERS = {
    "Origin": "www.udemy.com",
    # "User-Agent":
    # "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Accept": "*/*",
    "Accept-Encoding": None,
}

SUBSCRIBED_COURSES_URL = "https://{portal_name}.udemy.com/api-2.0/users/me/subscribed-courses/?ordering=-last_accessed&fields[course]=@min,visible_instructors,image_240x135,favorite_time,archive_time,completion_ratio,last_accessed_time,enrollment_time,is_practice_test_course,features,num_collections,published_title,is_private,is_published,buyable_object_type&fields[user]=@min,job_title&page={page}&page_size={page_size}&is_archived={include_archived}"
COURSE_SEARCH_URL = "https://{portal_name}.udemy.com/api-2.0/users/me/subscribed-courses/?ordering=-last_accessed&fields[course]=archive_time,buyable_object_type,completion_ratio,enrollment_time,favorite_time,features,image_240x135,image_480x270,is_practice_test_course,is_private,is_published,last_accessed_time,num_collections,published_title,title,tracking_id,url,visible_instructors&fields[user]=@min,job_title&page={page}&page_size={page_size}&search={search}&is_archived={include_archived}"
COURSE_INFO_URL = "https://{portal_name}.udemy.com/api-2.0/courses/{course_id}/"
COURSE_CURRICULUM_URL = "https://{portal_name}.udemy.com/api-2.0/courses/{course_id}/cached-subscriber-curriculum-items?fields[asset]=results,title,external_url,time_estimation,download_urls,slide_urls,filename,asset_type,captions,media_license_token,course_is_drmed,media_sources,stream_urls,body&fields[chapter]=object_index,title,sort_order&fields[lecture]=id,title,object_index,asset,supplementary_assets,view_html&page={page}&page_size={page_size}"
