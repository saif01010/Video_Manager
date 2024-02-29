import sqlite3

connection = sqlite3.connect('video_manager.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        duration INTEGER NOT NULL
    )
''')

def list_videos():
    print('\n')
    print('*' * 40)
    print('Here are all the videos:')
    cursor.execute('SELECT * FROM videos')
    for video in cursor.fetchall():
        print(video)
    print('*' * 40)
    
def add_videos(name,duration):
    cursor.execute('''
        INSERT INTO videos(title, duration)
        VALUES(?, ?)
    ''', (name, duration))
    connection.commit()
    print('Video added successfully')

def update_videos(video_id, name, duration):
    cursor.execute('''
        UPDATE videos
        SET title = ?, duration = ?
        WHERE id = ?
    ''', (name, duration, video_id))
    connection.commit()
    print('Video updated successfully')

def delete_videos(video_id):
    cursor.execute('''
        DELETE FROM videos
        WHERE id = ?
    ''', (video_id,))
    connection.commit()
    print('Video deleted successfully')

def main():
    print('Welcome to Video Manager!')
    while True:
        print('1. List all video')
        print('2. add a video')
        print('3. update a videos')
        print('4. Delete a video')
        print('5. Exit')
        option = input('Select an option: ')
        if option == '1':
            list_videos()
        elif option == '2':
            name = input('Enter the name of the video: ')
            duration = input('Enter the duration of the video: ')
            add_videos(name, duration)
        elif option == '3':
            video_id = input('Enter the id of the video: ')
            name = input('Enter the name of the video: ')
            duration = input('Enter the duration of the video: ')
            update_videos(video_id, name, duration)
        elif option == '4':
            video_id = input('Enter the id of the video: ')
            delete_videos(video_id)
        elif option == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid option')


if __name__ == '__main__':
    main()