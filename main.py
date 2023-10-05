''' main file '''

from application.server import Server

def main():
    ''' main function '''
    server = Server()
    server.run()

if __name__=="__main__":
    main()
