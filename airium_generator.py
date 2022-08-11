from airium import Airium

def generate_page(message, link): 
  a = Airium()

  a('<!DOCTYPE html>')
  with a.html():
    with a.head():
      a.title(_t='') 
      with a.style():
        a("""
          html{
            color: black;
            font-family: "Trebuchet MS", Helvetica, sans-serif;
            font-size: 20px;
            background-image: url(https://cdn.discordapp.com/attachments/777205933284655116/777358966845341706/059087i01.jpg)
          }
          main{
            margin: 50px;
            margin-top: 200px;
            margin-bottom: 450px;
            padding: 75px;
            border-radius: 10px;
            border: 5px solid black;
            background-color: white;
          }
        """)

    with a.main():
      with a.p():
        a(message)
        with a.a(href=link):
          a("URL")

      with a.a(href='https://hackathon-creaticafront.ashleyjlr.repl.co'):
        a('Back to Moods Make Music')

  return a