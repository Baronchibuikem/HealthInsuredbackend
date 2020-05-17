# ********************
# python imports
# ********************
import glob
import os
import shutil
import sys
#*********************
#vendor imports
#*********************
import requests
# ********************
# app imports
# ********************

EXCEPTION_MSG_ERROR_SAVING_USER_MEDIA_FILE="EXCEPTION_MSG_ERROR_SAVING_USER_MEDIA_FILE"

EXCEPTION_MSG_ERROR_RENAMING_USER_MEDIA_FILE="EXCEPTION_MSG_ERROR_RENAMING_USER_MEDIA_FILE"

EXCEPTION_MSG_ERROR_DELETING_USER_MEDIA_FILE="EXCEPTION_MSG_ERROR_DELETING_USER_MEDIA_FILE"

def save_to_url_user_media(param_url,param_allowed_file_types,file_obj, file_type, uuid_file_name):
    """
    save a user uploaded media file
    """

    media_files_uri = param_url
    allowed_file_types = param_allowed_file_types

    # save image
    save_to_url_media_file(
        file_obj,
        uuid_file_name,
        file_type,
        allowed_file_types,
        media_files_uri
    )

def get_dirs_names(dir_path):
    """
    get the directories names in a path

    Args
        :param dir_path: path to the dir
    Returns:
        :rtype list: a list of the dirctories in the path
    """
    Py_Filling_Module_wrapper = Py_Filling_Wrapper()

    return Py_Filling_Module_wrapper.get_dir_names(dir_path)

def read_file(file_path):
    """
    read a file on a file path on disk

    Args
        :param file_path: path to the file
    Returns:
        :rtype string|byte: string or byte content of the file
    """
    Py_Filling_Module_wrapper = Py_Filling_Wrapper()

    return Py_Filling_Module_wrapper.read_file(file_path)

def stream_read_file(url,temp_file_dir,file_name):
    """
    read a file by streaming it from a url,
    save to a temporary file,read into a memory and delete the file

    Args
        :param url: url to the json file
        :param temp_file_dir: path to the temporay file directory
        :param file_name: name.ext of the file
    Returns:
        :rtype string|byte: string or byte content of the file
    """
    Requests_Filling_Module_wrapper = Requests_Filling_Wrapper()

    return Requests_Filling_Module_wrapper.stream_read_file(url,temp_file_dir,file_name)

def save_to_url_media_file(file_obj, file_name, file_type, allowed_types, save_url):
    """
    save application media files
    """
    Module_wrapper=Requests_Filling_Wrapper()

    try:
        Module_wrapper.save_to_url_media_file(file_obj, file_name, file_type, allowed_types, save_url)
    except Exception:
        raise Exception(EXCEPTION_MSG_ERROR_SAVING_USER_MEDIA_FILE)

def save_to_dir_media_file(file_obj, file_name, file_type, allowed_types, save_dir):
    """
    save application media files
    """
    Module_wrapper=Py_Filling_Wrapper()

    try:
        Module_wrapper.save_to_dir_media_file(file_obj, file_name, file_type, allowed_types, save_dir)
    except Exception as e:
        raise Exception(EXCEPTION_MSG_ERROR_SAVING_USER_MEDIA_FILE)

def rename_in_dir_media_file(file_dir, old_name, new_name):
    """
    rename a file
    """

    Module_wrapper=Py_Filling_Wrapper()

    try:
        Module_wrapper.rename_in_dir_media_file(file_dir, old_name, new_name)
    except Exception as e:
        raise Exception(EXCEPTION_MSG_ERROR_RENAMING_USER_MEDIA_FILE)

def delete_from_dir_media_file(file_dir, file_name):
    """
    delete a file
    """

    Module_wrapper=Py_Filling_Wrapper()

    try:
        Module_wrapper.delete_from_dir_media_file(file_dir, file_name)
    except Exception as e:
        raise Exception(EXCEPTION_MSG_ERROR_DELETING_USER_MEDIA_FILE)

class Py_Filling_Wrapper(object):
    """
    wrapper class for python file functions
    """
    def get_dirs_names(self,dir_path):
        """
        get the directories names in a path

        Args
            :param dir_path: path to the dir
        Returns:
            :rtype list: a list of the dirctories in the path
        """
        if (os.path.isdir(dir_path)):
            return os.listdir(dir_path)
        else:
            Exception_message=("path {0} for directories search does not exist").format(dir_path)
            raise Exception(Exception_message)

    def read_file(self,file_path):
        """
        read a file on a file path on disk

        Args
            :param file_path: path to the file
        Returns:
            :rtype string|byte: string or byte content of the file
        """
        #check file path exists
        if (os.path.isfile(file_path)):
            try:
                #open the file
                with open(file_path,"r+") as File_path:
                    #read the file object
                    File_content=File_path.read()
                    #return file content
                    return File_content
            except Exception as e:
                raise e
        else:
            Exception_message=("FILE>>>[{0}] does not exist").format(file_path)
            raise Exception(Exception_message)

    def save_to_dir_media_file(self,file_obj, file_name, file_type, allowed_types, save_dir):
        """
        save application media files
        """

        if file_type in allowed_types:
            # compose the file path if extension is among list of acceptable types
            File_path = os.path.join(save_dir, file_name + "." + file_type)

            # read and write the file
            with open(File_path, 'wb+') as des:
                des.write(file_obj)
            return True
        else:
            raise Exception("media file type not allowed")

    def rename_in_dir_media_file(self,file_dir, old_name, new_name):
        """
        rename a file
        """

        # old file path and name
        Old_dir_path = os.path.join(file_dir, old_name)

        # match extension to any three characters ie png or jpg
        Old_file_path = glob.glob(Old_dir_path + ".???")

        # new file path and name
        New_dir_path = os.path.join(file_dir, new_name)

        # match extension to any three characters ie png or jpg
        New_file_path = glob.glob(New_dir_path + ".???")

        # rename file
        if os.path.isfile(Old_file_path[0]):
            shutil.move(Old_file_path[0], New_file_path[0])
        else:
            raise Exception("media id to rename does not exist")

    def delete_from_dir_media_file(self,file_dir, file_name):
        """
        delete a file
        """

        # path to the photo file without extension
        Dir_path = os.path.join(file_dir, file_name)

        # match extension to any three characters ie png or jpg
        File_path = glob.glob(Dir_path + ".???")

        # remove file
        if os.path.isfile(File_path[0]):
            os.remove(File_path[0])
        else:
            raise Exception("media to delete does not exist")

class Requests_Filling_Wrapper(object):
    """
    wrapper class for file functions using http requests
    """

    def stream_read_file(self,url,temp_file_dir,file_name):
        """
        read a file by streaming it from a url,
        save to a temporary file,read into a memory and delete the file

        Args
            :param url: url to the json file
            :param temp_file_dir: path to the temporay file directory
            :param file_name: name.ext of the file
        Returns:
            :rtype string|byte: string or byte content of the file
        """
        #FIELDS
        File_content=""
        File_path=os.path.join(temp_file_dir,file_name)

        try:
            #stream the json file with HTTP request
            Request_response=get(url,stream=True)
            #check file directory path exists
            if (os.path.isdir(temp_file_dir)):
                #create the temporary file for writing
                with open(File_path,"wb") as File_obj:
                    #read the streamed HTTP file raw content in iterated chunks
                    #reading 128kb per iteration
                    for File_chunk in Request_response.iter_content(chunk_size=128):
                        #write the stream chunks read into the temporary file instead of holding in memory
                        File_obj.write(File_chunk)
            else:
                raise Exception(("{0} dir does not exist").format(temp_file_dir))
            #check file path exists
            if (os.path.isfile(File_path)):
                #open the saved file
                with open(File_path,"r+") as File_obj:
                    #read the file object
                    File_content=File_obj.read()
                    #delete the temporary file
                os.remove(File_path)
                #return the file content
                return File_content
            else:
                raise Exception(("{0} file does not exist").format(File_path))
        except Exception as e:
            Exception_message=("[Util_filling(Exception)]=>{0}").format(str(e))
            raise Exception(Exception_message)

    def save_to_url_media_file(self,file_obj, file_name, file_type, allowed_types, save_url):
        """
        save application media files
        """

        if file_type in allowed_types:

            #read file
            file_read=file_obj.read()

            #save
            multipart_form_data={
                file_name:file_read
            }

            response=requests.post(save_url,files=multipart_form_data)

            if response.ok:
                if response.status_code!=200:
                    raise Exception("file not saved-status:"+response.status_code)
            else:
                raise Exception("error saving file")
        else:
            raise Exception("media file type not allowed")