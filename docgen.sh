for i in *.py
do 
  pydoc -w ${i%.*}
done

mv *.html doc
