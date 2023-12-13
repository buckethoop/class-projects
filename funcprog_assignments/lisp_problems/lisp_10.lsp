;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun pack-all-duplicates (lst)
  (pack-all-duplicates-helper lst '()))
(defun pack-all-duplicates-helper (lst result)
  (cond ((null lst) (reverse result))
        ((null result) (pack-all-duplicates-helper (cdr lst) (list (list (car lst)))))
        ((equal (car lst) (caar result))
         (pack-all-duplicates-helper (cdr lst) (cons (cons (car lst) (car result)) (cdr result))))
        (t (pack-all-duplicates-helper (cdr lst) (cons (list (car lst)) result)))))
(defun remove-non-duplicates (lst)
  (remove-if (lambda (sublist) (<= (length sublist) 1)) lst))
(defun pack-duplicates (lst)
  (remove-non-duplicates (pack-all-duplicates lst)))
