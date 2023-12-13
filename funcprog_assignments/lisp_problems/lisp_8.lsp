;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun remove-duplicates (lst)
  (remove-duplicates-helper lst '()))
(defun remove-duplicates-helper (lst result)
  (if (null lst)
      (reverse result)
      (if (member (car lst) result)
          (remove-duplicates-helper (cdr lst) result)
          (remove-duplicates-helper (cdr lst) (cons (car lst) result)))))
