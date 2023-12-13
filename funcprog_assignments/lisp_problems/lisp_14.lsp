;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun sublist (lst a b)
  (cond ((= a b) nil)
        ((> a b) (append (sublist-helper lst a (1- (length lst)))
                         (sublist-helper lst 0 b)))
        (t (sublist-helper lst a b))))

(defun sublist-helper (lst a b)
  (if (null lst)
      nil
      (cond ((= a 0) (cons (car lst) (sublist-helper (cdr lst) 0 (1- b))))
            ((= b 0) nil)
            (t (sublist-helper (cdr lst) (1- a) (1- b))))))
