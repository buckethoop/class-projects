;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun sublist (lst a b)
  (cond ((> a b) nil)
        ((= a b) nil)
        ((zerop a) (sublist-helper lst b))
        (t (sublist (cdr lst) (1- a) (1- b)))))

(defun sublist-helper (lst n)
  (cond ((null lst) nil)
        ((zerop n) lst)
        (t (sublist-helper (cdr lst) (1- n)))))
