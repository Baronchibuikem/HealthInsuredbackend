#********************
#python imports
#********************
import math

def paginate(total_items_count,items_per_page,page,use_array_slice=True):
    """
    paginate database query

    Args:
        :param total_items:the count of total data items
        :param items_per_page:
        :param page:
        :param use_array_slice:
    Returns:
        :rtype dict{no_of_pages,current_page,next_page,prev_page,offset,limit}:
    """
    values_dict={}

    sql_val=cal_sql_limit_stmt_values(total_items_count, items_per_page, page)

    values_dict["no_of_pages"]=sql_val["no_of_pages"]
    values_dict["current_page"]=page

    if (page+1) > sql_val["no_of_pages"]:
        values_dict["next_page"]=0
    else:
        values_dict["next_page"]= page + 1
    if page !=0:
        values_dict["prev_page"]= page - 1
    else:
        values_dict["prev_page"]=page

    if use_array_slice==True:
        slice_val=cal_array_slice(sql_val["sql_offset"], sql_val["sql_limit"])
        values_dict["offset"]=slice_val["slice_start"]
        values_dict["limit"]=slice_val["slice_end"]
    else:
        values_dict["offset"]=sql_val["sql_offset"]
        values_dict["limit"]=sql_val["sql_limit"]
    return values_dict

def cal_sql_limit_stmt_values(total_items_count,items_per_page,page):
    """
    calculate sql LIMIT statement offset,limit values
    """
    #get the required number of pages to display
    No_of_pages=math.ceil(total_items_count/items_per_page)
    #calculate where to start retrieving
    offset= (items_per_page * page) - items_per_page
    limit=items_per_page
    Values_dict={}
    Values_dict["no_of_pages"]=No_of_pages
    Values_dict["sql_offset"]=offset
    Values_dict["sql_limit"]=limit
    return Values_dict

def cal_array_slice(sql_offset,items_per_page):
    """
    calculate array slice values from sql LIMIT values
    """
    ArraySliceStart=sql_offset
    ArraySliceEnd=sql_offset+items_per_page
    ValuesDict={}
    ValuesDict["slice_start"]=ArraySliceStart
    ValuesDict["slice_end"]=ArraySliceEnd
    return ValuesDict