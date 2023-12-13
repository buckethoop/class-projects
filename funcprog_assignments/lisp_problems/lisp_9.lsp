;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun pack-duplicates (lst)
  (pack-duplicates-helper lst '()))
(defun pack-duplicates-helper (lst result)
  (if (null lst)
      (reverse result)
      (if (null result)
          (pack-duplicates-helper (cdr lst) (list (list (car lst))))
          (if (equal (car lst) (caar result))
              (pack-duplicates-helper (cdr lst) (cons (cons (car lst) (car result)) (cdr result)))
              (pack-duplicates-helper (cdr lst) (cons (list (car lst)) result))))))    
