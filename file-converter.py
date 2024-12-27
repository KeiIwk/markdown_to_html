import sys
import markdown

def convert_markdown_to_html(input_file,output_file):
    try:
        with open(input_file,'r',encoding='utf-8') as infile:
            markdown_text=infile.read()
        html_content=markdown.markdown(markdown_text)

        with open(output_file,'w',encoding='utf-8') as outfile:
            outfile.write(html_content)
        print(f"Successfully converted '{input_file}' to '{output_file}'.")
    
    except Exception as e:
        print(f"Error:{e}")

def main():
    if len(sys.argv)!=4 or sys.argv[1]!='markdown':
        print("Usage: python3 file-converter.py markdown <inputfile> <outputfile>")
        sys.exit(1)
    
    input_file=sys.argv[2]
    output_file=sys.argv[3]
    convert_markdown_to_html(input_file,output_file)

if __name__ == '__main__':
    main()