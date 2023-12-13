;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun remove-all (lst elem)
  (if (null lst)
      '()
      (if (equal (car lst) elem)
          (remove-all (cdr lst) elem)
          (cons (car lst) (remove-all (cdr lst) elem)))))
