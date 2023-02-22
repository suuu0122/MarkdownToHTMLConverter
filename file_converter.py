import markdown
import os
import sys

def validate_args():
    num_arguments = len(sys.argv)
    if (num_arguments != 4):
        print("Wrong arguments num!")
        print("USAGE: python3 file_converter.py markdown input_file output_file")
        sys.exit()

    using_method = sys.argv[1]
    if (using_method != "markdown"):
        print("Wrong using method name")
        print("USAGE: python3 file_converter.py markdown input_file output_file")
        sys.exit()

    input_file_path = sys.argv[2]
    is_file = os.path.isfile(input_file_path)
    root_ext_pair_input_file = os.path.splitext(input_file_path)
    if (not is_file):
        print("Wrong input file name!")
        sys.exit()
    if (root_ext_pair_input_file[1] != ".md"):
        print("Wrong file extension! Input file extension is .md")
        sys.exit()

    output_file_path = sys.argv[3]
    root_ext_pair_output_file = os.path.splitext(output_file_path)
    if (root_ext_pair_output_file[1] != ".html"):
        print("Wrong file extension! Output file extension is .html")
        sys.exit()

def main():
    validate_args()
    input_file_path = sys.argv[2]
    output_file_path = sys.argv[3]
    
    with open(input_file_path) as input_f:
        text = input_f.read()
    html = markdown.markdown(text)
    
    with open(output_file_path, 'w') as output_f:
        output_f.write(html)
        
if __name__ == "__main__": 
    main()
