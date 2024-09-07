import os, shutil

# Define the file types and their associated extensions and file names
file_types = {
    'Images': {
        'Extensions': ['ai', 'bmb', 'gif', 'ico', 'jpeg', 'jpg', 'max', 'obj', 'png', 'ps', 'psd', 'svg', 'tif', 'tiff', '3ds', '3dm'],
        'File Names': ['AI Image (ai)', 'Bitmap Image (bmb)', 'Graphics Interchange Format (gif)', 'Icon File (ico)', 'Joint Photographic Experts Group (jpeg)', 'JPEG Image (jpg)', 'Autodesk 3ds Max Scene (max)', 'Wavefront OBJ File (obj)', 'Portable Network Graphics (png)', 'PostScript (ps)', 'Photoshop Document (psd)', 'Scalable Vector Graphics (svg)', 'Tagged Image File Format (tif)', 'TIFF Image (tiff)', '3D Studio Scene (3ds)', 'Rhino 3D Model (3dm)']
    },
    'Text Files': {
        'Extensions': ['doc', 'docx', 'odt', 'msg', 'pdf', 'rtf', 'tex', 'txt', 'wks', 'wps', 'wpd'],
        'File Names': ['Word Document (doc)', 'Word Document (docx)', 'Open Document Text (odt)', 'Outlook Message (msg)', 'Portable Document Format (pdf)', 'Rich Text Format (rtf)', 'LaTeX Document (tex)', 'Plain Text (txt)', 'Microsoft Works Document (wks)', 'Microsoft Works Document (wps)', 'WordPerfect Document (wpd)']
    },
    'Executable Files': {
        'Extensions': ['apk', 'bat', 'bin', 'cgi', 'com', 'exe', 'jar', 'py', 'wsf', 'ipynb'],
        'File Names': ['Android Package (apk)', 'Batch File (bat)', 'Binary File (bin)', 'Common Gateway Interface Script (cgi)', 'Command File (com)', 'Executable File (exe)', 'Java Archive (jar)', 'Python Script (py)', 'Windows Script File (wsf)', 'Jupyter Notebook (ipynb)']
    },
    'Audio Files': {
        'Extensions': ['aif', 'cda', 'iff', 'mid', 'midi', 'mp3', 'mpa', 'wav', 'wma', '3g2', '3gp'],
        'File Names': ['Audio Interchange File Format (aif)', 'Compact Disc Audio Track (cda)', 'Interchange File Format (iff)', 'MIDI File (mid)', 'MIDI File (midi)', 'MP3 Audio File (mp3)', 'MPEG Audio (mpa)', 'Waveform Audio File Format (wav)', 'Windows Media Audio (wma)', '3GPP2 Multimedia File (3g2)', '3GPP Multimedia File (3gp)']
    },
    'Video Files': { 
        'Extensions': ['mp4', 'avi', 'flv', 'mkv', 'mov', 'wmv'],
        'File Names': ['MPEG-4 Video File (mp4)', 'Audio Video Interleave (avi)', 'Flash Video (flv)', 'Matroska Video File (mkv)', 'Apple QuickTime Movie (mov)', 'Windows Media Video (wmv)']
    },
    'Spreadsheets': {
        'Extensions': ['ods', 'xlr', 'xls', 'xlsx'],
        'File Names': ['OpenDocument Spreadsheet (ods)', 'Microsoft Works Spreadsheet (xlr)', 'Microsoft Excel Spreadsheet (xls)', 'Microsoft Excel Spreadsheet (xlsx)']
    },
    'Presentations': {
        'Extensions': ['key', 'odp', 'pps', 'ppt', 'pptx'],
        'File Names': ['Keynote Presentation (key)', 'OpenDocument Presentation (odp)', 'PowerPoint Slide Show (pps)', 'PowerPoint Presentation (ppt)', 'PowerPoint Presentation (pptx)']
    },
    'Database Files': {
        'Extensions': ['accdb', 'csv', 'dat', 'db', 'dbf', 'log', 'mdb', 'pdb', 'sav', 'sql', 'tar'],
        'File Names': ['Access Database (accdb)', 'Comma-Separated Values (csv)', 'Data File (dat)', 'Database File (db)', 'Database File (dbf)', 'Log File (log)', 'Microsoft Database (mdb)', 'Palm Desktop Database (pdb)', 'SPSS Data File (sav)', 'Structured Query Language (sql)', 'Tape Archive (tar)']
    },
    'Web Files': {
        'Extensions': ['asp', 'aspx', 'cer', 'cfm', 'cgi', 'pl', 'css', 'htm', 'html', 'js', 'part', 'php', 'rss', 'xhtml'],
        'File Names': ['Active Server Pages (asp)', 'Active Server Page Executable (aspx)', 'Security Certificate (cer)', 'ColdFusion Markup Language File (cfm)', 'Common Gateway Interface Script (cgi)', 'Perl Script (pl)', 'Cascading Style Sheet (css)', 'Hypertext Markup Language (htm)', 'Hypertext Markup Language (html)', 'JavaScript File (js)', 'Partially Downloaded File (part)', 'Hypertext Preprocessor (php)', 'Really Simple Syndication (rss)', 'Extensible Hypertext Markup Language (xhtml)']
    },
    'System Files': {
        'Extensions': ['bak', 'cab', 'cfg', 'cpl', 'cur', 'dll', 'dmp', 'drv', 'icns', 'ico', 'ini', 'lnk', 'msi', 'sys', 'tmp'],
        'File Names': ['Backup File (bak)', 'Windows Cabinet File (cab)', 'Configuration File (cfg)', 'Control Panel Extension (cpl)', 'Cursor File (cur)', 'Dynamic Link Library (dll)', 'Dump File (dmp)', 'Device Driver (drv)', 'Icon File (icns)', 'Icon File (ico)', 'Configuration File (ini)', 'Shortcut (lnk)', 'Windows Installer Package (msi)', 'System File (sys)', 'Temporary File (tmp)']
    }
}


def get_path():
    '''
    Get the folder path from the user.
    This function prompts the user to enter a folder path, checks if the path exists, and returns the path if valid.

    Returns:
        path (str): The valid folder path entered by the user.
    '''

    path = input("Enter path (e.g., C:\\Users\\): ")

    if not os.path.exists(path): raise ValueError("Path does not exist.")
    
    return path

def organize_files(folder_path):
    '''
    Organize files into their corresponding folders based on extensions.
    This function reads the files from the provided folder path, checks their extensions, and moves them into categorized folders.

    Args:
        folder_path (str): The path of the folder containing files to be organized.

    Returns:
        None
    '''
    try:
        count_move = 0
        list_of_files = os.listdir(folder_path)  # List all files in the given folder
        
        for file in list_of_files:
            extension = file.split('.')[-1].lower()  # Get the file extension
            
            for category, data in file_types.items():
                if extension in data['Extensions']:
                    index = data['Extensions'].index(extension)
                    file_name = data['File Names'][index]

                    category_path = os.path.join(folder_path, category)
                    specific_path = os.path.join(category_path, file_name)

                    if not os.path.exists(specific_path):
                        os.makedirs(specific_path)  # Create the folder if it doesn't exist

                    source = os.path.join(folder_path, file)
                    destination = os.path.join(specific_path, file)
                    
                    shutil.move(source, destination)  # Move the file to the new location
                    print(f"'{file}' moved to '{file_name}'")
                    count_move += 1
                    break
        
        print(f"Total files moved: {count_move}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    try:
        folder_path = get_path()  # Get the folder path from the user
        organize_files(folder_path)
        print("File Organize successfully")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
  