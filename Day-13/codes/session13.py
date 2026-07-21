from dbHelper import DBHelper
def main():
    db=DBHelper()
    db.select_collection()
    condition={
        'email':'mannat@gmail.com'   }
    update_data={
        'email':'mannat43@gmail.com'
    }
    db.update(condition,update_data)
    db.retrieve()
if __name__ == '__main__':
    main()